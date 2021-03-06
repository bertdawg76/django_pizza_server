# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0007_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_count', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_name', models.CharField(max_length=100)),
                ('side_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='sidenumber',
            name='sides',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Sides'),
        ),
        migrations.AddField(
            model_name='order',
            name='sides',
            field=models.ManyToManyField(blank=True, through='pizza.SideNumber', to='pizza.Sides'),
        ),
    ]
