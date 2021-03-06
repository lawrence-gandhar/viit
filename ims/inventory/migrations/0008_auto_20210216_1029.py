# Generated by Django 3.1.6 on 2021-02-16 04:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20210122_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeemaster',
            options={'verbose_name_plural': 'Employee'},
        ),
        migrations.AlterModelOptions(
            name='projectmaster',
            options={'verbose_name_plural': 'Project'},
        ),
        migrations.AlterModelOptions(
            name='subsidiarymaster',
            options={'verbose_name_plural': 'Subsidiary'},
        ),
        migrations.AlterField(
            model_name='device',
            name='PO_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 4, 59, 47, 355115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 4, 59, 47, 356118, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='host_name',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='history_log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 4, 59, 47, 363126, tzinfo=utc)),
        ),
    ]
