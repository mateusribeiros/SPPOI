from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao

@csrf_exempt
def index(request):
    template = render(request, 'index.html')
    return template

@csrf_exempt
def render_lab(request):
    mProjects = Projeto.objects.all().values()

    context = {
        'mProjects': mProjects
    }

    template = render(request,'lab.html', context)
    return template