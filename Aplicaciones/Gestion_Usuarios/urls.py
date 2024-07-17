from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarUsuarios/', views.registrarUsuarios),
    path('edicionUsuario/<telefono>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('eliminarUsuarios/<telefono>', views.eliminarUsuarios),
    path('enviarNotifi/<telefono>/<nombreC>/<mensaje>', views.enviarNotifi),
]