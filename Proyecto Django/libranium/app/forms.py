from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(attrs={"form-control"}))

    class Meta:
        model=Contacto
        fields = ["nombre", "email", "tipo", "mensaje"]

