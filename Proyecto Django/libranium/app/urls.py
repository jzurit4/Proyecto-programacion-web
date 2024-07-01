from django.urls import path
from .views import home, comprar, Crec_Personal, formulario, juvenil, libro1, Lit_Chilena, Nosotros, \
    novelas, poesia, ubicacion, login, Cuenta, registro,agregarProducto, listar_productos, modificar_producto

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
    path('agregar-producto/', agregarProducto, name="agregarProducto"),
    path('listar-producto/',listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
]