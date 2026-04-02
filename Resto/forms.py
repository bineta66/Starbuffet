# Resto/forms.py
from django import forms
from .models import Traiteur

class TraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = ['nomcomplet', 'specialites', 'description',  'experience','adresse', 'email', 'telephone', 'image', 'est_actif']