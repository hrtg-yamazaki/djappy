# Generated by Django 2.2.6 on 2020-01-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djappy', '0002_auto_20200117_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=4095),
        ),
    ]
