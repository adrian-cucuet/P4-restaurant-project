# Generated by Django 4.2 on 2023-04-17 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_reservation_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_people',
            field=models.CharField(choices=[('one', '1 Person'), ('two', '2 People'), ('three', '3 People'), ('four', '4 People'), ('five_plus', '5+ People')], default='one', max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
