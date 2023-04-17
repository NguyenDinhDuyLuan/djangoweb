from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .form import ProjectForm

# projectItem = [
#     {
#         'idProduct': '1',
#         'nameProduct': 'Product 1',
#         'infoProduct': 'Info for Items 1',
#         'pricesProduct': '14.56',
#         'state': True
#     },
#     {
#         'idProduct': '2',
#         'nameProduct': "Product 2",
#         'infoProduct': "Info for Items 2",
#         'pricesProduct': "76.56",
#         'state': False
#     },
#     {
#         'idProduct': '3',
#         'nameProduct': "Product 3",
#         'infoProduct': "Info for Items 3",
#         'pricesProduct': "24.56",
#         'state': True
#     },
#     {
#         'idProduct': '4',
#         'nameProduct': "Product 4",
#         'infoProduct': "Info for Items 4",
#         'pricesProduct': "17.56",
#         'state': True
#     }
# ]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'websites/projects.html', context)


def pageTwo(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.review_set.all()
    context = {'project': projectObj, 'tags': tags, 'reviews': reviews}
    return render(request, 'websites/single-project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'websites/project-form.html', context)