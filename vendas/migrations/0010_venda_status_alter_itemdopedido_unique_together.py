# Generated by Django 4.0.5 on 2022-07-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_preco_custo'),
        ('vendas', '0009_remove_venda_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(choices=[('AB', 'Aberta'), ('FC', 'Fechada'), ('PR', 'Processando'), ('DC', 'Desconhecido')], default='DC', max_length=2),
        ),
        migrations.AlterUniqueTogether(
            name='itemdopedido',
            unique_together={('venda', 'produto')},
        ),
    ]
