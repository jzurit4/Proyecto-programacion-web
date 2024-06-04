from django.urls import path
from .views import home, comprar, Crec_Personal, cuenta, formulario, juvenil, libro1, Lit_Chilena, Nosotros, novelas, poesia, ubicacion

urlpatterns = [
    path('', home, name="home"),
    path('Crec_Personal/', Crec_Personal, name="Crec_Personal"),
    path('comprar/', comprar, name="comprar"),
    path('cuenta/', cuenta, name="cuenta"),
    path('formulario/', formulario, name="formulario"),
    path('juvenil/', juvenil, name="juvenil"),
    path('libro1/', libro1, name="libro1"),
    path('Lit_Chilena/', Lit_Chilena, name="Lit_Chilena"),
    path('Nosotros/', Nosotros, name="Nosotros"),
    path('novelas/', novelas, name="novelas"),
    path('poesia/', poesia, name="poesia"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    
]