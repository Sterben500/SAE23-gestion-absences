from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import EtudiantsForm
from django.forms.models import model_to_dict

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = EtudiantsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appabs/etudiants/affiche/")
        return render(request, "appabs/ajoutetu.html", {"form": form})
    else:
        form = EtudiantsForm()
        return render(request, "appabs/ajoutetu.html", {"form": form})

def affiche(request):
    etudiants = models.Etudiants.objects.all()
    return render(request, "appabs/afficheetu.html", {"etudiants": etudiants})

def modif(request, id):
    etudiants = models.Etudiants.objects.get(pk=id)
    form = EtudiantsForm(model_to_dict(etudiants))
    return render(request, "appabs/modifetu.html", {"form": form, "id": id})

def supprimer(request, id):
    etudiants = models.Etudiants.objects.get(pk=id)
    etudiants.delete()
    return HttpResponseRedirect("/appabs/main/")

def updatesauvegarder(request, id):
    eform = EtudiantsForm(request.POST)
    if eform.is_valid():
        etudiants = eform.save(commit=False)
        etudiants.idetudiants = id
        etudiants.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutetu.html", {"form": eform, "id": id})