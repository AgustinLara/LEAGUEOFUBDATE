# Generated by Django 4.1.3 on 2022-12-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLOL', '0007_alter_items_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajes',
            name='buffonerfeo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personajes',
            name='modificaciones',
            field=models.CharField(max_length=100),
        ),
    ]
