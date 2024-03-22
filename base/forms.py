from django import forms
from base.models import CadastroAdotantes
class CadastroAdotante(forms.ModelForm):
    class Meta:
        model = CadastroAdotantes
        fields = ['nome', 'email','senha']
        widgets = {'senha': forms.PasswordInput()}