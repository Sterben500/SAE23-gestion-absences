from django.shortcuts import render
from . import models


# Create your views here.

def main(request):
    absences = models.Absences.objects.all()
    return render(request, "appabs/main.html",{"absences": absences})
