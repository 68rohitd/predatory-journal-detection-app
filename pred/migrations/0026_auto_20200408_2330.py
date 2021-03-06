# Generated by Django 3.0.3 on 2020-04-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0025_auto_20200311_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journaltable2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_journal', models.CharField(max_length=200)),
                ('Links', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Old_new', models.CharField(max_length=200)),
                ('email_of_editor', models.CharField(max_length=200)),
                ('impact_factor', models.CharField(max_length=200)),
                ('number_of_editors', models.CharField(max_length=200)),
                ('review_time', models.CharField(max_length=200)),
                ('review_process', models.CharField(max_length=200)),
                ('journal_website', models.CharField(max_length=200)),
                ('fast_track_fee', models.CharField(max_length=200)),
                ('author_fee_for_subscription_model', models.CharField(max_length=200)),
                ('author_fee_for_open_access', models.CharField(max_length=200)),
                ('charging_for_readers_for_open_access', models.CharField(max_length=200)),
                ('journal_name', models.CharField(max_length=200)),
                ('conflicts_of_interest', models.CharField(max_length=200)),
                ('revenue_sources', models.CharField(max_length=200)),
                ('journal_archive', models.CharField(max_length=200)),
                ('publishing_schedule', models.CharField(max_length=200)),
                ('copyright_info', models.CharField(max_length=200)),
                ('journal_index', models.CharField(max_length=200)),
                ('publisher_info', models.CharField(max_length=200)),
                ('type_of_peer_review', models.CharField(max_length=200)),
                ('clarity_of_abstract_Internation_Journal', models.CharField(max_length=200)),
                ('clarity_of_abstract_Regional_Journal', models.CharField(max_length=200)),
                ('quality_of_and_comformity_with_stated_aim', models.CharField(max_length=200)),
                ('readability_of_article', models.CharField(max_length=200)),
                ('content_availability', models.CharField(max_length=200)),
                ('english_language_homepage_availability_International_journal', models.CharField(max_length=200)),
                ('regional_language_homepage_availability_Regional_journal', models.CharField(max_length=200)),
                ('If_open_access_is_it_listed_in_directory_of_open_access_journal', models.CharField(max_length=200)),
                ('affiliation_of_editors', models.CharField(max_length=200)),
                ('diversity_in_geographical_distribution_of_editors', models.CharField(max_length=200)),
                ('diversity_in_geographical_distribution_of_authors', models.CharField(max_length=200)),
                ('plagiarism', models.CharField(max_length=200)),
                ('similarity_of_website_design', models.CharField(max_length=200)),
                ('editors_standing', models.CharField(max_length=200)),
                ('convincing_editorial_scope', models.CharField(max_length=200)),
                ('send_jornal_spam_email_to_review_papers', models.CharField(max_length=200)),
                ('questionable_special_issue', models.CharField(max_length=200)),
                ('Predatory_1_Non_predatory_0', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='journaltable',
            name='predatory',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Affiliation_of_Editor',
            field=models.CharField(choices=[('Affiliation_of_Editor', '-----'), ('2', 'Full affiliation'), ('1', 'Only country name'), ('0', 'Not Available')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Email_of_Editor',
            field=models.CharField(choices=[('Email_of_Editor', '-----'), ('2', 'Official'), ('1', 'general Email Service'), ('0', 'Not Available')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Number_of_Editors',
            field=models.CharField(choices=[('Number_of_Editors', '-----'), ('2', 'More than 7'), ('1', 'Between 5-7'), ('0', 'Lower than 5')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Review_Time',
            field=models.CharField(choices=[('Review_Time', '-----'), ('2', 'More than a month'), ('1', 'Lower than a month'), ('0', 'Lower than a week')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable',
            name='Using_bogus_metric_and_index',
            field=models.CharField(choices=[('Using_bogus_metric_and_index', '-----'), ('1', 'No'), ('0', 'Yes')], max_length=200),
        ),
    ]
