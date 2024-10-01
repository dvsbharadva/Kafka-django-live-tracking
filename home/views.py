from django.shortcuts import render
from django.http import JsonResponse
from .models import LocationUpdate
# Create your views here.

def index(request):
    return render(request, "index.html")

def get_data(request):
    latest_data = LocationUpdate.objects.latest('timestamp')
    return JsonResponse({
        'latitude' : latest_data.latitude,
        'longitude' : latest_data.longitude,
        'timestamp' : latest_data.timestamp,
    })