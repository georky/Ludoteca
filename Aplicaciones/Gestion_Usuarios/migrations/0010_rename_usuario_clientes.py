# Generated by Django 5.0.7 on 2024-08-11 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Usuarios', '0009_alter_usuario_campo11'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Clientes',
        ),
    ]