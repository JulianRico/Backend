# Generated by Django 4.2.5 on 2023-09-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0002_alter_promocion_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='promocion',
            name='department',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
