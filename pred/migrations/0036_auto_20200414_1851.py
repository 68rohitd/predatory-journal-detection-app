# Generated by Django 3.0.3 on 2020-04-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0035_auto_20200414_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='parameter',
        ),
        migrations.AddField(
            model_name='journal',
            name='parameter',
            field=models.ManyToManyField(to='pred.Parameter'),
        ),
    ]
