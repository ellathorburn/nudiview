# Generated by Django 4.0.3 on 2022-04-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_alter_report_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='comments',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
