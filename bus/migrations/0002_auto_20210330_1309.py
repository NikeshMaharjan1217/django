# Generated by Django 3.1.7 on 2021-03-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_purchased',
            name='ticket_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket_purchased',
            name='ticket_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket_purchased',
            name='ticket_rate',
            field=models.IntegerField(default=0),
        ),
    ]
