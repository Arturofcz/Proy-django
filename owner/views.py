from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from owner.forms import OwnerForm
from owner.models import Owner
from django.db.models import F, Q

from django.views.generic import ListView, DeleteView, CreateView, UpdateView


# Serializador
from django.core import serializers as ssr

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
    owners = Owner.objects.all()

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
    #owners = Owner.objects.all()[2:8]

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

    print("Query: {}".format(query))
    results = (
        Q(nombre__icontains=query)


    )

    data_context = Owner.objects.filter(results).distinct()

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})

def owner_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    owners = Owner.objects.all()
    return render(request, 'owner/owners_details.html', context={'data': owners})

def owner_create(request):
    # request.method = "POST"
    if request.method == "POST":
        print("ES UN POST")
        form = OwnerForm(request.POST)
        if form.is_valid():
            # nombre = form.cleaned_data['nombre']
            # print("Nombre: {}".format(nombre))
            # edad = form.cleaned_data['edad']
            # pais = form.cleaned_data['pais']
            try:
                form.save()
                return redirect('owner_list')
            except:
                pass
    else:
        form = OwnerForm()
    return render(request, 'owner/owner-create.html', {'form': form})

def owner_delete(request, id_owner):
    print("ID: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()
    return redirect('owner_detail')

def owner_edit(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_detail')

    return render(request, 'owner/owner_update.html', {'form': form})

"""Vistas basadas en clases"""
"""ListView, CreateView, UpdateView, DeleteView"""
class OwnerList(ListView):
    #permission_classes = [IsAuthenticated]
    model = Owner
    template_name = 'owner/owner_vc.html'

class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner-create.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner-update-vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc')
    template_name = 'owner/owner-confirm-delete.html'

"""Serializers"""
def ListOwnerSerializer(request):
    lista = ssr.serialize('json', Owner.objects.all(), fields=['nombre', 'pais', 'edad'])
    return HttpResponse(lista, content_type="application/json")
