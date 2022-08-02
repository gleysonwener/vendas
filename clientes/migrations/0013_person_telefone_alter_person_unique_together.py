# Generated by Django 4.0.5 on 2022-07-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_alter_person_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('first_name', 'telefone')},
        ),
    ]
