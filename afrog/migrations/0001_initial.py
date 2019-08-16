# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-16 07:31
from __future__ import unicode_literals

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=260)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(default=0, max_length=14)),
                ('pic', models.ImageField(blank=True, upload_to='profilepics2/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
