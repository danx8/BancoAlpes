from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def terminosycondiciones(request):
    return render(request, 'terminosYCondiciones.html')

