# Generated by Django 5.1.1 on 2024-12-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_carbrandmodel_alter_carmodel_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbrandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]