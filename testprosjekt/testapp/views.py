from django.shortcuts import render
from django.http import HttpResponse
from .models import Hund, Eier
from django.db.models import Count

# Create your views here.
def index(request):
    hunder = Hund.objects.all()
    context = {'hunder' : hunder}
    return render(request, 'testapp/index.html', context)

def eierliste(request):
    eiere = Eier.objects.all()
    context={'eier' : eiere}
    return render(request, 'testapp/eierliste.html', context)

def eier(request):
    eiere = Eier.objects.annotate(antall_hunder=Count('hund'))
    context = {
        'eiere': eiere
    }
    return render(request, 'testapp/eier.html', context)

def hundedetaljer(request):
    if request.method=='POST':
        eier = request.POST.get('detaljer')
        hunder = Hund.objects.filter(eier=eier)
        context = {'hunder' : hunder}
        return render(request, 'testapp/hundedetaljer.html', context)
