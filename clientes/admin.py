from django.contrib import admin

from .models import Person, Documento


#from actions import nfe_emitida, nfe_nao_emitida


class PersonAdmin(admin.ModelAdmin):
    exclude = ('bio',)
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'photo')
    search_fields = ('id', 'first_name')
    autocomplete_fields = ['doc']



class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)


admin.site.site_header = 'Gestão Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Sejam Bem vindo ao Gestão Clientes'