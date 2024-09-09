from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'Website/home.html')

def about(request):
    return render(request,'Website/about.html')


def contact(request):
    return render(request,'Website/contact.html')


