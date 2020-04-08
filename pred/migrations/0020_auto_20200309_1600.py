# Generated by Django 3.0.3 on 2020-03-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0019_remove_journaltable_to_be_listed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaltable',
            name='Affiliation_of_Editor',
            field=models.CharField(choices=[('Affiliation of Editor', '-----'), ('2', 'Full affiliation'), ('1', 'Only country name'), ('0', 'Not Available')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Email_of_Editor',
            field=models.CharField(choices=[('Email of Editor', '-----'), ('2', 'Official'), ('1', 'general Email Service'), ('0', 'Not Available')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Number_of_Editors',
            field=models.CharField(choices=[('Number of Editor', '-----'), ('2', 'More than 7'), ('1', 'Between 5-7'), ('0', 'Lower than 5')], max_length=200),
        ),
    ]
