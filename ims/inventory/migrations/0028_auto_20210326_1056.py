# Generated by Django 3.1.3 on 2021-03-26 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_auto_20210326_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
