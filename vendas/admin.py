from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class VendasAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ("pessoa",)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'numero', 'pessoa', 'nfe_emitida', 'valor')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemPedidoInLine]

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(Venda, VendasAdmin)
admin.site.register(ItemDoPedido)
