from django.urls import path
from .views import home, masinfo, nosotros

urlpatterns = [
    path('', home, name='home'),
    path('masinfo/', masinfo, name='masinfo'),
    path('nosotros/', nosotros, name='nosotros'),
]
