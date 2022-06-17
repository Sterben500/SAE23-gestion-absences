from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import CoursForm
from django.forms.models import model_to_dict

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appabs/cours/affiche/")
        return render(request, "appabs/ajoutcours.html", {"form": form})
    else:
        form = CoursForm()
        return render(request, "appabs/ajoutcours.html", {"form": form})

def affiche(request):
    cours = models.Cours.objects.all()
    return render(request, "appabs/affichecours.html", {"cours": cours})

def modif(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = CoursForm(model_to_dict(cours))
    return render(request, "appabs/modifcours.html", {"form": form, "id": id})

def supprimer(request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("/appabs/main/")

def updatesauvegarder(request, id):
    cform = CoursForm(request.POST)
    if cform.is_valid():
        cours = cform.save(commit=False)
        cours.idcours = id
        cours.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutcours.html", {"form": cform, "id": id})