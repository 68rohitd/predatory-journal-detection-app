# Generated by Django 3.0.3 on 2020-02-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0006_auto_20200225_1637'),
    ]

    operations = [
        migrations.DeleteModel(
            name='metricTable',
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Affiliation_of_Editor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Availablity_of_Journal_Full_Address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Charging_both_authors_and_readers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Email_of_Editor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Fastrack_Fee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Number_of_Editors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Number_of_Paper_in_each_issue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Publication_Fee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Questionable_special_issue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Review_Time',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Send_journal_spam_Email_to_recieve_papers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Submission_Fee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Unclear_Review_Process',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journaltable',
            name='Using_bogus_metric_and_index',
            field=models.BooleanField(default=False),
        ),
    ]
