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


# Trang web chính: Hiển thịnh table project
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'websites/projects.html', context)


# Trang web thứ 2, hiển thị thông tin chi tiết của project
def pageTwo(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.review_set.all()
    context = {'project': projectObj, 'tags': tags, 'reviews': reviews}
    return render(request, 'websites/single-project.html', context)


# chức năng tạo project: cho phép người dùng tạo và nhập giá trị vô database
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'websites/project-form.html', context)


# chức năng cập nhật dữ liệu, cho phép xem và thay đổi thông tin của project
def updateProject(request, pk):
    context = {}
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    template = 'websites/project-form.html'

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()  # save instance
            return redirect('projects')

    context['form'] = form
    return render(request, template, context)


def deleteProject(request, pk):
    """Return a foobang
    Optional plotz says to frobnicate the bizbaz first.
    """
    project = Project.objects.get(id=pk)
    template = 'websites/delete.html' 

    # phần code xử lý POST request
    if request.method == 'POST':
        project.delete()  # xóa instance
        return redirect('projects')

    return render(request, template, {'object': project})
