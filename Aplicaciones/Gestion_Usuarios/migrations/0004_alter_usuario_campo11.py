# Generated by Django 5.0.7 on 2024-07-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Usuarios', '0003_alter_usuario_campo11'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='campo11',
            field=models.DateTimeField(null=True),
        ),
    ]
