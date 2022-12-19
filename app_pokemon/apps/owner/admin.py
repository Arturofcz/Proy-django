from django.contrib import admin
from .models import Owner


# Register your models here.
# admin.site.register(Owner)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','pais','dni')  #configura los datos que se va a visualizar en la lista de registros
    search_fields = ('nombre', 'pais') #agrega un campo de busqueda
    list_filter = ('edad',) # agrega un campo para filtrar a lado derecho
    # fields = ('nombre','edad')
