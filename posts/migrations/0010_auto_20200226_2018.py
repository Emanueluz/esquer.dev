# Generated by Django 3.0.1 on 2020-02-26 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200226_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lock_key',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
