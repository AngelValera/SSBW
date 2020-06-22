# Generated by Django 3.0.7 on 2020-06-19 08:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitas_granada', '0003_auto_20200619_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='owner',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='visita', to=settings.AUTH_USER_MODEL),
        ),
    ]