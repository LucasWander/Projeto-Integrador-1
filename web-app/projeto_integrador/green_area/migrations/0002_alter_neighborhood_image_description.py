# Generated by Django 5.1 on 2024-09-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green_area', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood_image',
            name='description',
            field=models.CharField(max_length=40),
        ),
    ]