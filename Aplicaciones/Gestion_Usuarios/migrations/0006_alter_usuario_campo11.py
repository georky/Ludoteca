# Generated by Django 5.0.7 on 2024-07-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Usuarios', '0005_alter_usuario_campo1_alter_usuario_campo12_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='campo11',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]