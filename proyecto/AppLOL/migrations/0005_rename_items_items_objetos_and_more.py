# Generated by Django 4.1.3 on 2022-12-17 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppLOL', '0004_rename_items_comunity_campeon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='items',
            new_name='objetos',
        ),
        migrations.RenameField(
            model_name='personajes',
            old_name='campeon',
            new_name='campeonLOL',
        ),
    ]
