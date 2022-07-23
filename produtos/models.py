from django.db import models


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco_custo = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao + ' - ' + str(self.preco_custo) + ' - ' + str(self.preco)

