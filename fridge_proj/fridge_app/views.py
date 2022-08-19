from django.shortcuts import render
from .models import *

def index(request):
    food_list = Food.objects.all()
    return render(request, 'index.html', { 'food_list': food_list })
