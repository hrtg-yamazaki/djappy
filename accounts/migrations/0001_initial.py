# Generated by Django 2.2.6 on 2020-01-19 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, choices=[('男性', '男性'), ('女性', '女性'), ('非公開', '非公開')], default='非公開', max_length=10, null=True)),
                ('introduction', models.TextField(blank=True, max_length=140, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
