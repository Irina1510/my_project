# Generated by Django 5.0 on 2023-12-17 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=50)),
                ('photos', models.CharField(max_length=20)),
                ('price_per_night', models.FloatField(default=100)),
                ('available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room', to='catalog.hotel')),
            ],
        ),
    ]
