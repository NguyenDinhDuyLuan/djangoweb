from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

projectItem = [
    {
        'idProduct': '1',
        'nameProduct': 'Product 1',
        'infoProduct': 'Info for Items 1',
        'pricesProduct': '14.56',
        'state': True
    },
    {
        'idProduct': '2',
        'nameProduct': "Product 2",
        'infoProduct': "Info for Items 2",
        'pricesProduct': "76.56",
        'state': False
    },
    {
        'idProduct': '3',
        'nameProduct': "Product 2",
        'infoProduct': "Info for Items 3",
        'pricesProduct': "24.56",
        'state': True
    },
    {
        'idProduct': '4',
        'nameProduct': "Product 1",
        'infoProduct': "Info for Items 4",
        'pricesProduct': "17.56",
        'state': True
    }
]


def projects(request):
    name = 'Duy Luan'
    age = 23

    context = {'projects': projectItem}
    return render(request, 'websites/projects.html', context)


def pageTwo(request, pk):
    projectObject = None

    for i in projectItem:
        if i['idProduct'] == str(pk):
            projectObject = i

    return render(request, 'websites/single-project.html', {'project': projectObject})
