# Generated by Django 4.1.7 on 2023-03-27 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_cliente_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='image',
        ),
    ]
