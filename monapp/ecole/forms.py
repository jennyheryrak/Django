from django import forms
from .models import Eleve

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nomcomplet', 'age', 'sexe', 'datenaissance']