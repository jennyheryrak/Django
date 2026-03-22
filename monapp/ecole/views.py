from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleve
from .forms import EleveForm

# Create your views here.
def home(request):
    eleve = Eleve.objects.all()
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = EleveForm()

    return render(request, 'ecole/index.html', {
        'eleve': eleve,
        'form': form,
    })

def supprimer(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    eleve.delete()
    return redirect('accueil')

def modifier(request, id):
    eleve = get_object_or_404(Eleve, pk=id)

    if request.method == 'POST':
        form = EleveForm(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = EleveForm(instance=eleve)

    return render(request, 'ecole/eleve_form.html', {'form': form})