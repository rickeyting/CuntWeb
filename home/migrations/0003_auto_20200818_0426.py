# Generated by Django 2.0.7 on 2020-08-17 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_fix_history_motor_plate_motor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motor_plate',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.motor_type'),
        ),
    ]
