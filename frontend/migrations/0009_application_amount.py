# Generated by Django 5.0.6 on 2024-07-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_applicationlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
