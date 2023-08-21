from django.contrib import admin
from django.urls import path
from gestion import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('inicio_sesion/', auth_views.LoginView.as_view(
        template_name='inicio_sesion.html'), name='inicio_sesion'),
    path('registrarse/', views.register, name='registrarse'),
    path('buscar/', views.buscar_libros, name="buscar_libros"),
    path('busqueda_avanzada/', views.busqueda_avanzada, name='busqueda_avanzada'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro,
         name='eliminar_libro'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
