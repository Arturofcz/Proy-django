from django.shortcuts import render

from owner.models import Owner
from django.db.models import F, Q

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
    # owners = [
    #     {
    #         'nombre_owner': 'Daniel Ordeno',
    #         'edad': 24,
    #         'pais': 'Peru',
    #         'dni': '12345678',
    #         'vigente': True
    #     },
    #     {
    #         'nombre_owner': 'Arturo Callupe',
    #         'edad': 38,
    #         'pais': 'Brasil',
    #         'dni': '45292668',
    #         'vigente': True
    #     },
    #     {
    #         'nombre_owner': 'Katty Perez',
    #         'edad': 30,
    #         'pais': 'Chile',
    #         'dni': '42345679',
    #         'vigente': True
    #     },
    #     {
    #         'nombre_owner': 'Hugo Campos',
    #         'edad': 28,
    #         'pais': 'Paraguay',
    #         'dni': '41785267',
    #         'vigente': True
    #     },
    # ]

    """Crear un objeto en la base de datos de la tabla owner"""
    # p = Owner(nombre="Rossmery", pais="España",edad=21)
    # p.save()  # Guarda el registro en la base de datos
    #
    # p.nombre = "Beatriz"
    # p.save()

    """Obtener todos los elementos de una tabla en la bd"""
    # owners = Owner.objects.all()

    """filtracion de datos: filter()"""

    # owners = Owner.objects.filter(nombre="Luis")

    """filtracion de datos con AND  de sql: filter """
    # owners = Owner.objects.filter(nombre="Beatriz", edad=21)

    """filtracion de datos mas precisos con __contains"""

    # owners = Owner.objects.filter(nombre__contains="Beatriz")

    """filtracion de datos mas precisos con __endswith"""
    # owners = Owner.objects.filter(nombre__endswith="go")

    """Ordenoar por cualquier atributo o campo en la base de datos"""
    #owners = Owner.objects.order_by('-edad')


    """Acortar concatenamos diferentes metodos deeORMs"""
    owners = Owner.objects.all()[2:8]

    """Eliminando un conjunto de datos especificos"""
   # p = Owner.objects.filter(id=9)
    # p.delete() # elimina el reistor ue encontro

    """Actualizacion de datos en la BD a un cierto grupo de datos"""
    # Owner.objects.filter(pais__startswith="Chi").update(edad=36)

    """Utilizando F expresions"""
    # Owner.objects.filter(edad__gte=30).update(edad=F('edad')+10)

    """Consultas complejas"""
    # query = Q(pais__startswith='Pe') | Q(pais__startswith='Br')
    # owners = Owner.objects.filter(query)

    """Negar Q"""
    # query = Q(pais__startswith='Pe') & ~Q(edad=21)
    # owners = Owner.objects.filter(query)

    # query = Q(pais__startswith='Pe') & Q(pais__startswith='Br')
    # owners = Owner.objects.filter(query, edad=21)

    """Errror de consulta Q no es valido """
    # query = Q(pais__startswith='Pe') & Q(pais__startswith='Br')
    # owners = Owner.objects.filter(edad=21, query)

    return render(request, 'owner/owners.list.html', context={'data': owners})



def owner_search(request):
    query = request.GET.get('q', '')

    results = (
        Q(nombre__icontains=query)
    )

    data_context = Owner.objects.filter(results).distinct()

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})