# Generated by Django 3.1 on 2021-11-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsummary', '0003_auto_20211113_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsummary',
            name='type_summary',
            field=models.IntegerField(choices=[(0, 'KLGBcuochop '), (1, 'KLGBvanhanh'), (2, 'KLGB_DTXD_SCL'), (3, 'KLGBKhac')], null=True),
        ),
    ]