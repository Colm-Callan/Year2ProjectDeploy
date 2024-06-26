# Generated by Django 5.0.2 on 2024-02-27 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Euro Order Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=255)),
                ('billingAddress1', models.CharField(blank=True, max_length=255)),
                ('billingCity', models.CharField(blank=True, max_length=255)),
                ('billingPostcode', models.CharField(blank=True, max_length=10)),
                ('billingCountry', models.CharField(blank=True, max_length=200)),
                ('shippingName', models.CharField(blank=True, max_length=255)),
                ('shippingAddress1', models.CharField(blank=True, max_length=255)),
                ('shippingCity', models.CharField(blank=True, max_length=255)),
                ('shippingPostcode', models.CharField(blank=True, max_length=10)),
                ('shippingCountry', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Euro Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
