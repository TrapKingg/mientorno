from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
def index(request):
    return render(request, 'index/index.html')