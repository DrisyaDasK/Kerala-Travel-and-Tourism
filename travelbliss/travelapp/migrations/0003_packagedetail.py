# Generated by Django 5.0.3 on 2024-03-22 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_packages'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_description', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('package_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.packages')),
            ],
        ),
    ]