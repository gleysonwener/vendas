# Generated by Django 4.0.5 on 2022-06-15 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_alter_venda_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuário pode alterar NFe'), ('ver_dashboard', 'Pode visualizar a dashboard'), ('permissao3', 'Permissão 3'))},
        ),
    ]
