from django.urls import path
from .views import home, masinfo, nosotros, agregar_producto, listar_productos, modificar_producto, eliminar_producto

urlpatterns = [
    path('', home, name='home'),
    path('masinfo/', masinfo, name='masinfo'),
    path('nosotros/', nosotros, name='nosotros'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
]
