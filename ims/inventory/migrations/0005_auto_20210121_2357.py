# Generated by Django 2.1.7 on 2021-01-21 18:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210121_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_status',
            field=models.CharField(choices=[('Initiated', 'Initiated'), ('Completed', 'Completed')], default='Initiated', max_length=50),
        ),
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 27, 0, 46268, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 27, 0, 46268, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 27, 0, 46268, tzinfo=utc)),
        ),
    ]