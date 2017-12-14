# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessname', models.CharField(max_length=32, verbose_name='业务线名称')),
            ],
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, verbose_name='主机名')),
                ('port', models.CharField(max_length=10, verbose_name='端口')),
                ('busid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.BusinessInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=32, verbose_name='密码')),
                ('email', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserType'),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='mm',
            field=models.ManyToManyField(to='app01.UserInfo'),
        ),
    ]
