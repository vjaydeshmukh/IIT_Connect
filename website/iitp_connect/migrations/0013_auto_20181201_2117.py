# Generated by Django 2.1.2 on 2018-12-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iitp_connect', '0012_auto_20181201_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_status',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=1, max_length=2),
        ),
    ]
