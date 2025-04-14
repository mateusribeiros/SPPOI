from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.timezone import now
from django.shortcuts import render
import pytz
import uuid
import json

CACHE_TIMEOUT_SECONDS = 60 * 60 * 24  # 24h
INDEX_KEY = 'temp_index'

def render_lab(request):
    template = render(request, 'system.html')
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
