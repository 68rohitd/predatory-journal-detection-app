# Generated by Django 3.0.3 on 2020-02-28 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0007_auto_20200226_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='journaltable',
            name='domain',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journaltable',
            name='topic',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
