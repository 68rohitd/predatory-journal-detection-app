# Generated by Django 3.0.3 on 2020-05-02 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0039_journaldatabase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='journl_name',
            new_name='journal_name',
        ),
    ]
