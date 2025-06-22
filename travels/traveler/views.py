from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Application page Traveler.")

def categories(request, order_id):
        return HttpResponse(f"<h1>Ariticle by categories.</h1><p>{order_id}</p>")