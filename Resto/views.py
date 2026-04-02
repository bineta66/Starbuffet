from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Traiteur
from django.shortcuts import render, redirect
from .forms import TraiteurForm 
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'main.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def cours(request):
    return render(request, 'cours.html')



def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    return render(request, 'traiteurs.html', {'traiteurs': traiteurs})

def contact(request):
    return render(request, 'contact.html')

def inscription_traiteur(request):
    return render(request, 'inscription-traiteur.html')

def detail_traiteur(request, id):
    traiteur = get_object_or_404(Traiteur, id=id)
    return render(request, 'detail.html', {'traiteur': traiteur})

@login_required(login_url='login')
def ajouter_traiteur(request):
    from .forms import TraiteurForm

    if request.method == 'POST':
        form = TraiteurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_traiteurs')
    else:
        form = TraiteurForm()

    return render(request, 'ajouter_traiteur.html', {'form': form})

def detail_traiteur(request, id):
    traiteur = Traiteur.objects.get(id=id)

    specialites_list = traiteur.specialites.split(',')

    return render(request, 'detail.html', {
        'traiteur': traiteur,
        'specialites_list': specialites_list
    })