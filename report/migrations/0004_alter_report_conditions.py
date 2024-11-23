# Generated by Django 4.0.3 on 2022-03-31 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_report_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='conditions',
            field=models.CharField(choices=[('Glassy', 'Glassy'), ('Fair', 'Fair'), ('Windy', 'Windy'), ('Rough', 'Rough')], default='Fair', max_length=10),
        ),
    ]