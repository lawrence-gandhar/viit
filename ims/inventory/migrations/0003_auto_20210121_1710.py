# Generated by Django 2.1.7 on 2021-01-21 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210121_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='Model_no',
            new_name='model_no',
        ),
        migrations.AddField(
            model_name='projectmaster',
            name='project_status',
            field=models.CharField(default='Active', max_length=20, verbose_name=(('Active', 'Active'), ('On_hold', 'On_hold'), ('Suspended', 'Suspended'), ('Completed', 'Completed'))),
        ),
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 11, 40, 31, 337599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 11, 40, 31, 337599, tzinfo=utc)),
        ),
    ]
