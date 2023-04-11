from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request):
    return render(request, 'websites/projects.html')

def pageTwo(request, pk):
    return render(request,'websites/single-project.html')