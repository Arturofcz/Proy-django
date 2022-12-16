from django.shortcuts import render

from owner.models import Owner


# Create your views here.

def owner_list(request):
    # data_context = {
    #     'nombre_owner': '',
    #     'edad': 18,
    #     'pais': 'Peru',
    #     'dni': '12345678',
    #     'vigente': False
    #
    # }
    #
    owners = [
        {
            'nombre_owner': 'Daniel Ordeno',
            'edad': 24,
            'pais': 'Peru',
            'dni': '12345678',
            'vigente': True
        },
        {
            'nombre_owner': 'Arturo Callupe',
            'edad': 38,
            'pais': 'Brasil',
            'dni': '45292668',
            'vigente': True
        },
        {
            'nombre_owner': 'Katty Perez',
            'edad': 30,
            'pais': 'Chile',
            'dni': '42345679',
            'vigente': True
        },
        {
            'nombre_owner': 'Hugo Campos',
            'edad': 28,
            'pais': 'Paraguay',
            'dni': '41785267',
            'vigente': True
        },
    ]

    """Crear un objeto en la base de datos de la tabla owner"""
    p = Owner(nombre="Rossmery", pais="España",edad=21)
    p.save()  # Guarda el registro en la base de datos

    p.nombre = "Beatriz"
    p.save()

    return render(request, 'owner/owners.list.html', context={'data': owners})