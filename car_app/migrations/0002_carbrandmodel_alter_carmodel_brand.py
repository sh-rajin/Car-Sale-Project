# Generated by Django 5.1.1 on 2024-12-15 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_app.carbrandmodel'),
        ),
    ]