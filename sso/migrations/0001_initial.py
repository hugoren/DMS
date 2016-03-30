# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_name', models.CharField(max_length=500, verbose_name=b'url\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url_url', models.CharField(max_length=500, verbose_name=b'url\xe5\x9c\xb0\xe5\x9d\x80')),
                ('url_parameter', models.CharField(max_length=500, verbose_name=b'url\xe5\x8f\x82\xe6\x95\xb0')),
                ('url_note', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Url_Permissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permissions_all', models.CharField(max_length=500, verbose_name=b'\xe5\x85\xa8\xe9\x83\xa8\xe6\x9d\x83\xe9\x99\x90')),
                ('permissions_customs', models.CharField(max_length=500, verbose_name=b'\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe6\x9d\x83\xe9\x99\x90')),
                ('permissions_note', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
