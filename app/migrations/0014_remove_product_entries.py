# Generated by Django 4.0.2 on 2022-03-29 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_brand_status_product_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='entries',
        ),
    ]
