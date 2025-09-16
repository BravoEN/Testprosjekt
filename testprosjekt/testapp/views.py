from django.shortcuts import render
from django.http import HttpResponse
from .models import Hund, Eier

# Create your views here.
def index(request):
    hunder = Hund.objects.all()
    context = {'hunder' : hunder}
    return render(request, 'testapp/index.html', context)

def eierliste(request):
    eier = Eier.objects.all()
    context={'eier' : eier}
    return render(request, 'testapp/eierliste.html', context)