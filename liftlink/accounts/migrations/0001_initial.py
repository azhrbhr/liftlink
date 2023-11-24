# Generated by Django 4.2.7 on 2023-11-23 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=15, unique=True)),
                ('license_number', models.CharField(max_length=20)),
                ('capacity', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')], max_length=20)),
                ('transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], max_length=20)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('truck', 'Truck'), ('suv', 'SUV'), ('motorcycle', 'Motorcycle')], max_length=20)),
                ('is_available', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
