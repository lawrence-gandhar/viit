# Generated by Django 3.1.3 on 2021-03-26 10:56

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0026_auto_20210326_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 56, 23, 813098, tzinfo=utc)),
        ),
    ]
