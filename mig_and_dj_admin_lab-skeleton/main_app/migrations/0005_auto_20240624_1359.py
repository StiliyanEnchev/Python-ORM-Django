# Generated by Django 5.0.4 on 2024-06-24 10:59
import random

from django.db import migrations

from main_app.models import Product


class Migration(migrations.Migration):

    def generate_barcodes(apps, schema_editor):
        products = apps.get_model('main_app', 'Product')
        all_products = Product.objects.all()
        barcodes = random.sample(range(100000000, 1000000000), len(all_products))
        for product, barcode in zip(all_products, barcodes):
            product.barcode = barcode
            product.save()

    def reverse_barcodes(apps, schema_editor):
        products = apps.get_model('main_app', 'Product')
        for product in Product.objects.all():
            product.barcode = 0
            product.save()

    dependencies = [
        ('main_app', '0004_product_barcode'),
    ]

    operations = [
        migrations.RunPython(generate_barcodes, reverse_barcodes)
    ]