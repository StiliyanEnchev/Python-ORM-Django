# Generated by Django 5.0.4 on 2024-07-10 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='car',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='main_app.car'),
        ),
    ]
