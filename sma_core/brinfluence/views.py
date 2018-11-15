from django.shortcuts import render
from .models import BrandCategory

# Create your views here.

def home(request):
    return render(request, 'brinfluence/home.html')