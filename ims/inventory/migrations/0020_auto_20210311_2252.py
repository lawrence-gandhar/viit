# Generated by Django 3.1.6 on 2021-03-11 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20210311_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 17, 21, 57, 342531, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 17, 21, 57, 343531, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 17, 21, 57, 347507, tzinfo=utc)),
        ),
    ]
