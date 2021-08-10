# Generated by Django 3.1.2 on 2021-08-10 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('CNIC', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='supplier.supplier')),
            ],
        ),
    ]
