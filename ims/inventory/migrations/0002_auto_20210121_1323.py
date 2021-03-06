# Generated by Django 2.1.7 on 2021-01-21 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 7, 53, 28, 774615, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='iepl_id',
            field=models.CharField(max_length=10, unique=True, verbose_name='iepl_id'),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 7, 53, 28, 774615, tzinfo=utc)),
        ),
    ]
