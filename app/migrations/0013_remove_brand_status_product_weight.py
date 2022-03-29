# Generated by Django 4.0.2 on 2022-03-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_order_discount_remove_order_due_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(choices=[('1', 'Box'), ('2', 'Pieces')], default=1, max_length=10),
        ),
    ]