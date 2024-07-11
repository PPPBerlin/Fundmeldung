from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import EigeneUserCreationForm
from . models import *

# Create your views here.

def fundmeldung(request):
    fundmeldung = Fundmeldung.objects.all()
    einmessungsart, lagezumortskern, lageimgelaende, gelaendenutzung, bodenart, befundart, zeitstellung, auffindungsart = Auswahllisten()
    f = {'fundmeldung': fundmeldung, 'lagezumortskern': lagezumortskern,
         'lageimgelaende': lageimgelaende, 'einmessungsart': einmessungsart,
         'gelaendenutzung': gelaendenutzung, "bodenart": bodenart, "befundart": befundart,
         "zeitstellung": zeitstellung, "auffindungsart": auffindungsart}
    return render(request, 'fundmeldung.html', f)

def linksammlung(request):
    linksammlungs = Linksammlung.objects.all()
    return render(request, 'linksammlung.html', {'linksammlungs': linksammlungs})

def start(request):
    return render(request, 'start.html')

def loginSeite(request):
    seite = 'login'
    if request.method == 'POST':
        benutzername = request.POST['benutzername']
        passwort = request.POST['passwort']

        benutzer = authenticate(request, username=benutzername, password=passwort)

        if benutzer is not None:
            login(request, benutzer)
            return redirect('start')
        else:
            messages.error(request, "Benutzername oder Passwort nicht korrekt!")

    return render(request, 'login.html', {'seite': seite})

def logoutBenutzer(request):
    logout(request)
    return redirect('start')

def regBenutzer(request):
    seite = 'reg'
    form = EigeneUserCreationForm

    if request.method == 'POST':
        form = EigeneUserCreationForm(request.POST)
        if form.is_valid():
            benutzer = form.save(commit=False)
            benutzer.save()

            kunde = Pfleger(name=request.POST['username'], benutzer=benutzer)
            kunde.save()

            login(request, benutzer)
            return redirect('start')
        else:
            messages.error(request, "Fehlerhafte Eingabe!")

    ctx = {'form': form, 'seite': seite}
    return render(request, 'login.html', ctx)