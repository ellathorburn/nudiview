# Generated by Django 4.0.3 on 2022-04-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_alter_siteweather_weather_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteweather',
            name='swell_marginal',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='siteweather',
            name='swell_max',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
