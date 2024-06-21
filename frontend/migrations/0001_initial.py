# Generated by Django 5.0.6 on 2024-06-21 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=40)),
                ('place', models.CharField(max_length=100)),
                ('bank_account_number', models.CharField(max_length=26)),
                ('payment_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.beneficiary')),
                ('payment_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.paymentlist')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentListBeneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.beneficiary')),
                ('payment_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.paymentlist')),
            ],
            options={
                'unique_together': {('payment_list', 'beneficiary')},
            },
        ),
        migrations.AddField(
            model_name='paymentlist',
            name='Beneficiaries',
            field=models.ManyToManyField(related_name='payments', through='frontend.PaymentListBeneficiary', to='frontend.beneficiary'),
        ),
    ]
