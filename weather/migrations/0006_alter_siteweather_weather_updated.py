# Generated by Django 4.0.3 on 2022-04-07 15:57

from django.db import migrations, models
import weather.models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_alter_siteweather_weather_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteweather',
            name='weather_updated',
            field=models.DateTimeField(default=weather.models.yesterday),
        ),
    ]
