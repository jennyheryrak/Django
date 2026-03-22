from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleve

# Create your views here.
def home(request):
    eleve = Eleve.objects.all()
    return render(request, 'ecole/index.html', {
        'eleve': eleve
    })

def supprimer(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    eleve.delete()
    return redirect('accueil')
