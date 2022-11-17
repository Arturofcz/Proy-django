from django.contrib import admin
from .models import Owner


# Register your models here.
# admin.site.register(Owner)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','pais')  #configura los datos que se va a visualizar en la lista de registros
    search_fields = ('nombre', 'pais')      #agrega un campo de busqueda
    fields = ('nombre','edad')
