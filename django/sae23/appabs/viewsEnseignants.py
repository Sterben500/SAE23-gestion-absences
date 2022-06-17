from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import EnseignantsForm
from django.forms.models import model_to_dict

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = EnseignantsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appabs/enseignants/affiche/")
        return render(request, "appabs/ajoutens.html", {"form": form})
    else:
        form = EnseignantsForm()
        return render(request, "appabs/ajoutens.html", {"form": form})

def affiche(request):
    enseignants = models.Enseignants.objects.all()
    return render(request, "appabs/afficheens.html", {"enseignants": enseignants})

def modif(request, id):
    enseignants = models.Enseignants.objects.get(pk=id)
    form = EnseignantsForm(model_to_dict(enseignants))
    return render(request, "appabs/modifens.html", {"form": form, "id": id})

def supprimer(request, id):
    enseignants = models.Enseignants.objects.get(pk=id)
    enseignants.delete()
    return HttpResponseRedirect("/appabs/main/")

def updatesauvegarder(request, id):
    eform = EnseignantsForm(request.POST)
    print(eform)
    if eform.is_valid():
        enseignants = eform.save(commit=False)
        enseignants.idenseignants = id
        enseignants.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutens.html", {"form": eform, "id": id})