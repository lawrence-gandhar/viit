# Generated by Django 3.1.6 on 2021-03-15 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_auto_20210311_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 14, 15, 55, 194617, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 14, 15, 55, 195617, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 14, 15, 55, 197615, tzinfo=utc)),
        ),
    ]
