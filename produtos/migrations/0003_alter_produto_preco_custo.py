# Generated by Django 4.0.5 on 2022-07-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_preco_custo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_custo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
