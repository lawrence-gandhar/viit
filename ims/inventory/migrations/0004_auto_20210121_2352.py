# Generated by Django 2.1.7 on 2021-01-21 18:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210121_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='Allocation_status',
            new_name='allocation_status',
        ),
        migrations.AddField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 22, 28, 695828, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='device',
            name='rent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 22, 28, 695828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 18, 22, 28, 695828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projectmaster',
            name='project_status',
            field=models.CharField(choices=[('Active', 'Active'), ('On_hold', 'On_hold'), ('Suspended', 'Suspended'), ('Completed', 'Completed')], default='Active', max_length=20),
        ),
    ]
