# Generated by Django 4.0.2 on 2022-03-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('profile_pic', models.FileField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
                ('comfirm_password', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
