# Generated by Django 5.0.6 on 2024-07-03 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='phone_num',
            field=models.BigIntegerField(default=0, max_length=9),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='place_of_residence',
            field=models.CharField(default='chuj', max_length=150),
        ),
        migrations.AddField(
            model_name='historicalbeneficiary',
            name='phone_num',
            field=models.BigIntegerField(default=0, max_length=9),
        ),
        migrations.AddField(
            model_name='historicalbeneficiary',
            name='place_of_residence',
            field=models.CharField(default='chuj', max_length=150),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='birth_date',
            field=models.DateField(default=datetime.date(2000, 3, 24)),
        ),
        migrations.AlterField(
            model_name='historicalbeneficiary',
            name='birth_date',
            field=models.DateField(default=datetime.date(2000, 3, 24)),
        ),
    ]
