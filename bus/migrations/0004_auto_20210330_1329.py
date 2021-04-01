# Generated by Django 3.1.7 on 2021-03-30 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_ticket_purchased_bus_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_purchased',
            name='bus_time',
            field=models.TimeField(default=datetime.datetime(2021, 3, 30, 13, 29, 11, 65651)),
        ),
        migrations.AlterField(
            model_name='ticket_purchased',
            name='purchased_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
