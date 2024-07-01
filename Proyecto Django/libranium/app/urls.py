from django.urls import path
from .views import home, comprar, Crec_Personal, formulario, juvenil, libro1, Lit_Chilena, Nosotros, \
    novelas, poesia, ubicacion, login, Cuenta, registro,agregar_producto, listar_productos, modificar_producto,eliminar_producto

urlpatterns = [
    path('', home, name="home"),
    path('Crec_Personal/', Crec_Personal, name="Crec_Personal"),
    path('comprar/', comprar, name="comprar"),
    path('formulario/', formulario, name="formulario"),
    path('juvenil/', juvenil, name="juvenil"),
    path('libro1/', libro1, name="libro1"),
    path('Lit_Chilena/', Lit_Chilena, name="Lit_Chilena"),
    path('Nosotros/', Nosotros, name="Nosotros"),
    path('novelas/', novelas, name="novelas"),
    path('poesia/', poesia, name="poesia"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('login/', login, name="login"),
    path('cuenta/', Cuenta, name="cuenta"),
    path('registro/',registro, name="registro"),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
]