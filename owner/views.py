from django.shortcuts import render


# Create your views here.

def owner_list(request):
    data_context = {
        'nombre_owner': 'kevin',
        'edad': 18,
        'pais': 'Peru',
        'vigente': True

    }

    return render(request, 'owners.list.html', context={'data': data_context})