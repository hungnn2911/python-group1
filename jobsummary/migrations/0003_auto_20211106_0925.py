# Generated by Django 3.1 on 2021-11-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsummary', '0002_auto_20211106_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='room_id',
        ),
        migrations.AddField(
            model_name='myuser',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobsummary.room'),
        ),
    ]
