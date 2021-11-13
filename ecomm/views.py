from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    datamap = {
        'data' : 10000,
        'kalimat' : "PROGANTARA"
    }
    return render(request, 'index.html', datamap)