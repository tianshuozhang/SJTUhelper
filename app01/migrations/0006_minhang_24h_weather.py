# Generated by Django 4.2.5 on 2023-10-06 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_seieenotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='minhang_24h_weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_weather_picture', models.CharField(max_length=100)),
                ('weather_text', models.CharField(max_length=100)),
                ('temperature', models.CharField(max_length=100)),
                ('wind_direction', models.CharField(max_length=100)),
                ('wind_strength', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
            ],
        ),
    ]