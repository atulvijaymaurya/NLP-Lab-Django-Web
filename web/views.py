from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import os
# Create your views here.
def index(request):
    template = loader.get_template('home.html')
    s = "Event List"
    context = {
        's' : s,
    }
    return render(request,'home.html',context)
def people(request):
    return render(request, 'people.html')
def publications(request):
    return render(request, 'publications.html')
def contactus(request):
    return render(request,'contactus.html')
def gallery(request):
    return render(request,'gallery.html')
def projects(request):
    return render(request,'projects.html')
def demos(request):
    return render(request,'demos.html')
def notfound(request):
    return render(request,'notfound.html')