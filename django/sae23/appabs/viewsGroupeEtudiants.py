from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import GroupeEtudiantForm
from django.forms.models import model_to_dict

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = GroupeEtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appabs/grpetudiants/affiche/")
        return render(request, "appabs/ajoutgrp.html", {"form": form})
    else:
        form = GroupeEtudiantForm()
        return render(request, "appabs/ajoutgrp.html", {"form": form})

def affiche(request):
    groupeetu = models.GroupeEtudiant.objects.all()
    return render(request, "appabs/affichegrp.html", {"groupeetu": groupeetu})

def modif(request, id):
    groupeetu = models.GroupeEtudiant.objects.get(pk=id)
    form = GroupeEtudiantForm(model_to_dict(groupeetu))
    return render(request, "appabs/modifgrp.html", {"form": form, "id": id})

def supprimer(request, id):
    groupeetu = models.GroupeEtudiant.objects.get(pk=id)
    groupeetu.delete()
    return HttpResponseRedirect("/appabs/main/")

def updatesauvegarder(request, id):
    gform = GroupeEtudiantForm(request.POST)
    if gform.is_valid():
        groupeetu = gform.save(commit=False)
        groupeetu.idgroupeetu = id
        groupeetu.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutgrp.html", {"form": gform, "id": id})