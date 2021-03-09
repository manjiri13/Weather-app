from django.shortcuts import render, HttpResponse, redirect
from .models import City
# from .forms import TaskForm
# Create your views here.
def index(request):
    
    return render(request, "index.html")
# Create your views here.
