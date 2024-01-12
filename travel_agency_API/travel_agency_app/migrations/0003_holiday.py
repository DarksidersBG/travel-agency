# Generated by Django 5.0.1 on 2024-01-10 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0002_travel_agency_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, verbose_name='Title')),
                ('startDate', models.DateField(verbose_name='Date')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('price', models.FloatField(verbose_name='Price')),
                ('freeSlots', models.IntegerField(verbose_name='Free slots')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.location')),
            ],
        ),
    ]
