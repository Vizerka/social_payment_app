# Generated by Django 5.0.6 on 2024-07-04 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_application_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('applications', models.ManyToManyField(related_name='application_lists', to='frontend.application')),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.benefit')),
            ],
        ),
    ]
