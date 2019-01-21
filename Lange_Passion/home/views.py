from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home</h1>")

def contacts(request):
    return HttpResponse("<h1>Contacts</h1>")

def watches(request):
    return HttpResponse("<h1>Watches</h1>")