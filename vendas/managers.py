from django.db import models
from django.db.models import Avg, Min, Max, Count


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desconto(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def minimo(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def maximo(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def num_ped(self):
        return self.all().aggregate(Count('id'))['id__count']

    def nun_ped_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']