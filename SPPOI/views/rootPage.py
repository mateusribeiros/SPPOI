from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = render(request, 'index.html')
    return template

# def render_save_page(request):
#     template = render(request, 'save.html')
#     return template