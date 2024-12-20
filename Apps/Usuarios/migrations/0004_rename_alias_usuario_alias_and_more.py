# Generated by Django 5.1.3 on 2024-11-24 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_usuario_alias_usuario_cvu_usuario_dinero_and_more'),
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Alias',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Dinero',
            new_name='dinero',
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='roles.rol'),
            preserve_default=False,
        ),
    ]
