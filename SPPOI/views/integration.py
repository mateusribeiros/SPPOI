from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.timezone import now
from django.shortcuts import render
import json
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao
