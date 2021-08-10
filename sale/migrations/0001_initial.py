# Generated by Django 3.1.2 on 2021-08-10 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('receipt_no', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('product_details', models.TextField(blank=True, help_text='Quantity and Product name would save in JSON format', max_length=512, null=True)),
                ('total_quantity', models.CharField(blank=True, default=1, max_length=10, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('remaining_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('cash_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('returned_payment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_sales', to='customer.customer')),
                ('extra_items', models.ManyToManyField(blank=True, max_length=200, to='product.ExtraItems')),
                ('purchased_items', models.ManyToManyField(blank=True, max_length=100, to='product.PurchasedProduct')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
