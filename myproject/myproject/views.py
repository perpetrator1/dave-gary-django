# from django.http import HttpResponse

from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! I'm  Home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Professional Ponderer, Part Time Developer")
    return render(request, 'about.html')