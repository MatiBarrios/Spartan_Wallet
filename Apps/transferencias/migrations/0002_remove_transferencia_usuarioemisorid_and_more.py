# Generated by Django 5.1.3 on 2024-11-24 02:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivos', '0001_initial'),
        ('transferencias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferencia',
            name='UsuarioEmisorId',
        ),
        migrations.AddField(
            model_name='transferencia',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transferencia',
            name='monto',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='motivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='motivos.motivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transferencia',
            name='usuarioEmisorMontoAnterior',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='usuarioReceptorId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_receptor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transferencia',
            name='usuarioReceptorMontoAnterior',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='usuarioEmisorId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_emisor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]