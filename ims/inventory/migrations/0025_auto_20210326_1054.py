# Generated by Django 3.1.3 on 2021-03-26 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0024_auto_20210326_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 10, 905275, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 10, 905577, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 10, 907356, tzinfo=utc)),
        ),
    ]
