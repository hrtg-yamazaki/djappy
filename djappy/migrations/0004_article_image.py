# Generated by Django 2.2.6 on 2020-01-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djappy', '0003_auto_20200117_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_images'),
        ),
    ]