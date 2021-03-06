# Generated by Django 3.1.7 on 2021-03-06 15:32

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesIncomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=450)),
                ('price', models.FloatField()),
                ('is_income', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SellsReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=255)),
                ('client_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('tax', models.IntegerField()),
                ('total_price', models.FloatField(default=2000000)),
                ('balance', models.FloatField(default=2000000)),
                ('payment_completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('item_sold', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.sellsreport')),
            ],
        ),
        migrations.CreateModel(
            name='PaidAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('item_sold', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.sellsreport')),
            ],
        ),
    ]
