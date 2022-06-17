from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import AbsencesForm
from django.forms.models import model_to_dict

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = AbsencesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appabs/absences/affiche/")
        return render(request, "appabs/ajoutabs.html", {"form": form})
    else:
        form = AbsencesForm()
        return render(request, "appabs/ajoutabs.html", {"form": form})

def affiche(request):
    absences = models.Absences.objects.all()
    return render(request, "appabs/afficheabs.html", {"absences": absences})

def modif(request, id):
    absences = models.Absences.objects.get(pk=id)
    form = AbsencesForm(model_to_dict(absences))
    return render(request, "appabs/modifabs.html", {"form": form, "id": id})

def supprimer(request, id):
    absences = models.Absences.objects.get(pk=id)
    absences.delete()
    return HttpResponseRedirect("/appabs/absences/affiche/")

def updatesauvegarder(request, id):
    aform = AbsencesForm(request.POST)
    if aform.is_valid():
        absences = aform.save(commit=False)
        absences.idabsences = id
        absences.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutabs.html", {"form": aform, "id": id})