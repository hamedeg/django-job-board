# Generated by Django 3.0.8 on 2020-07-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20200713_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]