# Generated by Django 3.0.3 on 2020-03-04 13:29

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas_granada', '0003_auto_20200304_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='foto',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/fotos'), upload_to=''),
        ),
    ]
