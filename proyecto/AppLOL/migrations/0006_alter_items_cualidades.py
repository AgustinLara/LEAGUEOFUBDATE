# Generated by Django 4.1.3 on 2022-12-17 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLOL', '0005_rename_items_items_objetos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='cualidades',
            field=models.CharField(max_length=40),
        ),
    ]