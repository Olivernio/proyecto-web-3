from django.urls import path
from . import views

urlpatterns = [
    path('login', views.iniciar_sesion, name='iniciar_sesion'),
    path('register', views.register, name='register'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('paginas_usuario/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('paginas_usuario/editar', views.editar, name='editar'),
    path('paginas_usuario/editar/<int:id>', views.editar, name='editar'),
    path('', views.index, name='index'),
    path('paginas_usuario/dan.html', views.dan_view, name='dan'),
    path('paginas_usuario/orang.html', views.orang_view, name='orang'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile, name='profile'),
]
