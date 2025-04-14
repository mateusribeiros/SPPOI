from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.timezone import now
from django.shortcuts import render
import json
from SPPOI.models import Sistema, Interface, EstiloIntegracao

def render_lab(request):
    mSistemas = Sistema.objects.all().values()

    context = {
        'mSistemas': mSistemas
    }

    template = render(request,'lab.html', context)
    return template

def register(request):
    template = render(request, 'registerSystem.html')
    return template

@csrf_exempt
def save(request):
    return "implementar"
    
@csrf_exempt
def update(request, id):
    return "implementar"

@csrf_exempt
def delete(request, id):
    return "implementar"
