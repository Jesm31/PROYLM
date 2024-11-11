# Generated by Django 5.1.3 on 2024-11-11 09:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_receta_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='favoritos',
            field=models.ManyToManyField(blank=True, related_name='favoritas', to=settings.AUTH_USER_MODEL),
        ),
    ]
