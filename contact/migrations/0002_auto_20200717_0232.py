# Generated by Django 3.0.8 on 2020-07-17 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='place',
            new_name='city',
        ),
        migrations.AddField(
            model_name='info',
            name='email_pio',
            field=models.CharField(default='Send us your query anytime!', max_length=60),
        ),
        migrations.AddField(
            model_name='info',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='work_hours',
            field=models.CharField(default='Mon to Fri 9am to 6pm', max_length=50),
        ),
    ]
