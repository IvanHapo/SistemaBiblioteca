from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Libro

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def buscar_libros(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        libros = Libro.objects.filter(titulo__icontains=query)
        return render(request, 'resultados_busqueda.html', {'libros': libros})
    return render(request, 'formulario_busqueda.html')


@login_required
def busqueda_avanzada(request):
    if request.method == 'GET':
        autor_nombre = request.GET.get('autor', '')
        genero = request.GET.get('genero', '')
        anio = request.GET.get('anio', '')

        consulta = Q()
        if autor_nombre:
            # Utiliza la relación ForeignKey__campo para buscar en campos relacionados
            consulta &= Q(autor__nombre__icontains=autor_nombre) | Q(
                autor__apellido__icontains=autor_nombre)
        if genero:
            consulta &= Q(genero__icontains=genero)
        if anio:
            consulta &= Q(anio_publicacion=anio)

        libros = Libro.objects.filter(consulta)
        return render(request, 'resultados_busqueda.html', {'libros': libros})


@login_required
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    print(libro_id)
    return render(request, 'detalle_libro.html', {'libro': libro})


@login_required
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    messages.success(request, 'El libro ha sido eliminado exitosamente.')
    if request.method == 'POST':
        libro.delete()
        return redirect('buscar_libros')


# Crear usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el usuario en la base de datos
            # Redireccionar al usuario a la vista de inicio de sesión
            return redirect('inicio_sesion')
    else:  # Evita que el usuario se salve el formulario o lo envie con errores
        form = UserCreationForm()
    return render(request, 'registrarse.html', {'form': form})


# Cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)
    # Redirigir a la página de inicio o a donde quieras
    return redirect('home')
