# Generated by Django 2.2.6 on 2020-01-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djappy', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, verbose_name='コメントの内容'),
        ),
    ]
