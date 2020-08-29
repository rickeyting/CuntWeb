# Generated by Django 2.0.7 on 2020-08-29 07:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200829_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motor_part',
            name='part_element',
            field=models.ManyToManyField(blank=True, to='home.motor_element'),
        ),
        migrations.AlterField(
            model_name='motor_plate',
            name='history',
            field=models.ManyToManyField(blank=True, to='home.fix_history'),
        ),
        migrations.AlterField(
            model_name='motor_plate',
            name='new_elements',
            field=models.ManyToManyField(blank=True, to='home.new_elements'),
        ),
        migrations.AlterField(
            model_name='motor_plate',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
