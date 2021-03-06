# Generated by Django 3.0.3 on 2020-04-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0026_auto_20200408_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaltable2',
            name='If_open_access_is_it_listed_in_directory_of_open_access_journal',
            field=models.CharField(choices=[('If_open_access_is_it_listed_in_directory_of_open_access_journal', '-----'), ('1', 'yes'), ('-1', 'no')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='Old_new',
            field=models.CharField(choices=[('Old_new', '-----'), ('1', 'Old'), ('0', 'New')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='Predatory_1_Non_predatory_0',
            field=models.CharField(choices=[('Predatory_1_Non_predatory_0', '-----'), ('1', 'yes'), ('0', 'no')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='affiliation_of_editors',
            field=models.CharField(choices=[('affiliation_of_editors', '-----'), ('1', 'full afflle'), ('-1', 'no affl avai')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='author_fee_for_open_access',
            field=models.CharField(choices=[('author_fee_for_open_access', '-----'), ('2', 'The journal clearly states the amount of money an author will pay to have each article published'), ('1', 'The journal states that an author fee is required but does not note how much it is.'), ('-1', 'The journal does not state whether or not there are any author fees'), ('0', 'Not open access model ')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='author_fee_for_subscription_model',
            field=models.CharField(choices=[('author_fee_for_subscription_model', '-----'), ('-1', 'The author is charged for publishing'), ('1', '  The author is not charged for publishing  '), ('0', ' It is not subscription model')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='charging_for_readers_for_open_access',
            field=models.CharField(choices=[('charging_for_readers_for_open_access', '-----'), ('-1', 'The reader is charged for reading'), ('0', 'The reader is not charge for reading/ it is not open access')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='clarity_of_abstract_Internation_Journal',
            field=models.CharField(choices=[('clarity_of_abstract_Internation_Journal', '-----'), ('-2', 'No abstract'), ('-1', 'Abstract non-English '), ('1', 'Abstract in English fairly clear '), ('2', 'Abstract in English very clear')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='clarity_of_abstract_Regional_Journal',
            field=models.CharField(choices=[('clarity_of_abstract_Regional_Journal', '-----'), ('-2', 'No abstract'), ('-1', 'Abstract in Non Regional Language'), ('1', 'Abstract in Regional Language, fairly clear'), ('2', 'Abstract in Regional Language, very clear')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='conflicts_of_interest',
            field=models.CharField(choices=[('conflicts_of_interest', '-----'), ('2', 'The journal thoroughly and clearly states a conflicts of interest policy, including how it will handle potential conflicts of interest of editors, authors, and reviewers'), ('1', 'The journal states a conflicts of interest policy, but the description of how conflicts will be handled is unclear'), ('-1', 'The journal does not state a conflicts of interest policy')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='content_availability',
            field=models.CharField(choices=[('content_availability', '-----'), ('-1', 'Recent content available online'), ('0', 'Recent content not available online')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='convincing_editorial_scope',
            field=models.CharField(choices=[('convincing_editorial_scope', '-----'), ('-2', 'not conv'), ('-1', ' poor'), ('0', 'fair'), ('1', 'good'), ('2', 'extreely god')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='copyright_info',
            field=models.CharField(choices=[('copyright_info', '-----'), ('1', "The journal clearly describes its copyright and licensing information on the journal's Web site, and licensing terms are indicated on the published articles (HTML/PDF)"), ('-1', " Copyright and licensing information is not found on the journal's Web site and on any published article")], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='diversity_in_geographical_distribution_of_authors',
            field=models.CharField(choices=[('diversity_in_geographical_distribution_of_authors', '-----'), ('-1', 'Regional diversity of authors board is not in line with editorial concept'), ('1', 'Regional diversity of authors board is partially in line with editorial concept'), ('2', 'Regional diversity of authors board is entirely in line with editorial concept')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='diversity_in_geographical_distribution_of_editors',
            field=models.CharField(choices=[('diversity_in_geographical_distribution_of_editors', '-----'), ('-2', 'No editorial board '), ('-1', 'Regional diversity of editorial board is not in line with editorial concept'), ('1', 'Regional diversity of editorial board is partially in line with editorial concept'), ('2', 'Regional diversity of editorial board is entirely in line with editorial concept')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='editors_standing',
            field=models.CharField(choices=[('editors_standing', '-----'), ('-2', 'extremely poor'), ('-1', ' poor'), ('0', 'fair'), ('1', 'good'), ('2', 'extreely god')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='email_of_editor',
            field=models.CharField(choices=[('email_of_editor', '-----'), ('-1', ' Not available'), ('1', 'General email service'), ('2', 'Official email')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='english_language_homepage_availability_International_journal',
            field=models.CharField(choices=[('english_language_homepage_availability_International_journal', '-----'), ('-2', 'not in eng'), ('-1', 'partially in eng'), ('1', 'entirely in eng')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='fast_track_fee',
            field=models.CharField(choices=[('fast_track_fee', '-----'), ('-1', ' Very High fast track fee'), ('1', '  Reasonable fee '), ('2', ' No Fee'), ('-2', ' doesnt mention')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='impact_factor',
            field=models.CharField(choices=[('impact_factor', '-----'), ('-2', 'Not available (if it’s an old journal)'), ('1', '0-1.5'), ('2', '1.5-3'), ('3', '3-4.5'), ('4', '4.5-6'), ('-1', 'None of these')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='journal_archive',
            field=models.CharField(choices=[('journal_archive', '-----'), ('2', 'The journal website contains an archive of its past issues with links to full text articles'), ('1', 'The journal website contains an archive but it may be incomplete or does not contain links to full text articles '), ('0', ' The journal does not have an archive of its past issues (new Journal )'), ('-1', ' The journal does not have an archive of its past issues (old Journal)')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='journal_index',
            field=models.CharField(choices=[('journal_index', '-----'), ('2', 'The journal is indexed in more than one subject database. (examples: ERIC, Google Scholar, Web of Science, PsycINFO) '), ('1', '  The journal is indexed in one subject database. (example: ERIC) '), ('-1', '  The journal is not indexed in a subject database')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='journal_name',
            field=models.CharField(choices=[('journal_name', '-----'), ('2', 'Name not confused with another journal '), ('1', 'The journal has a name similar to another journal but is able to be distinguished between the two.'), ('-1', 'The journal is unable to be distinguished from another with a similar name')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='journal_website',
            field=models.CharField(choices=[('journal_website', '-----'), ('3', ' The journal website is competently designed and functional. (examples: no broken links, easy navigation, no missing information)'), ('2', '  The journal website is adequately designed with passable functionality        . (examples: adequate navigation, few broken links, some missing information) '), ('1', ' The journal is poorly designed and is not functional. (examples: broken links, poor navigation, missing information)')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='number_of_editors',
            field=models.CharField(choices=[('number_of_editors', '-----'), ('0', 'Lower than 5'), ('1', 'Between 5-7'), ('2', 'More than 7'), ('-1', 'Doesn’t mention')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='plagiarism',
            field=models.CharField(choices=[('plagiarism', '-----'), ('2', '0% - 5\\% '), ('1', '5% - 10\\%'), ('-1', '10% - 50\\%'), ('-2', 'beyond 50\\%'), ('0', ' not mentin')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='publisher_info',
            field=models.CharField(choices=[('publisher_info', '-----'), ('1', ' Information about the ownership/management of the journal and contact information about the publisher is clearly identified'), ('-1', '   Information about the ownership/management of the journal and contact information about the publisher is not availabl')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='publishing_schedule',
            field=models.CharField(choices=[('publishing_schedule', '-----'), ('2', 'The journal clearly states how often its issues will be published each year and this agrees with the archive'), ('1', ' The journal does not state how often its issues will be published but it can be determined from the archive'), ('-1', 'The journal does not state how often its issues will be published each year and it cannot be determined from the archive ')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='quality_of_and_comformity_with_stated_aim',
            field=models.CharField(choices=[('quality_of_and_comformity_with_stated_aim', '-----'), ('1', ' Based on abstract, topic is covered clearly'), ('-1', 'Based on abstract, topic is not covered clearly '), ('-2', 'Based on abstract,  journal is not relevant')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='questionable_special_issue',
            field=models.CharField(choices=[('questionable_special_issue', '-----'), ('1', 'yes'), ('0', 'no')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='readability_of_article',
            field=models.CharField(choices=[('readability_of_article', '-----'), ('-1', 'Extremely Poor in sentence formation, Word usage, sentence beginnings and many grammatical mistakes '), ('1', 'Fairly good in sentence formation, Word usage, sentence beginnings and few  to none grammatical/spelling mistakes '), ('2', 'Excellent in sentence formation, Word usage, sentence beginnings and no grammatical mistakes')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='regional_language_homepage_availability_Regional_journal',
            field=models.CharField(choices=[('regional_language_homepage_availability_Regional_journal', '-----'), ('-2', 'not in reg lang'), ('-1', 'partially in reg lng'), ('1', 'entirely in reg lang')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='revenue_sources',
            field=models.CharField(choices=[('revenue_sources', '-----'), ('2', 'The journal clearly states its business model. This includes any revenue sources, like author fees, subscriptions, advertising, reprints, institutional support, and organizational support'), ('1', "The journal's business model lacks clarity when stating its revenue sources, like author fees, subscriptions, advertising, reprints, institutional support, and organizational support "), ('-1', ' The journal does not state its business model')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='review_process',
            field=models.CharField(choices=[('review_process', '-----'), ('2', ' The journal states whether it is peer reviewed/edited and has a review policy listed.'), ('1', '  The journal states whether it is peer reviewed/edited and has no review policy listed '), ('-1', ' The journal does not state whether it is peer reviewed/edited and has no review policy listed.')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='review_time',
            field=models.CharField(choices=[('review_time', '-----'), ('1', ' lower than week'), ('1', ' lower than month'), ('2', ' more than month'), ('-2', 'doesnt mention')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='send_jornal_spam_email_to_review_papers',
            field=models.CharField(choices=[('send_jornal_spam_email_to_review_papers', '-----'), ('-1', 'yes'), ('0', 'no')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='similarity_of_website_design',
            field=models.CharField(choices=[('similarity_of_website_design', '-----'), ('-1', 'Similar to other Website Designs'), ('1', 'uniqye Website Design')], max_length=200),
        ),
        migrations.AlterField(
            model_name='journaltable2',
            name='type_of_peer_review',
            field=models.CharField(choices=[('type_of_peer_review', '-----'), ('-2', ' No-peer-review'), ('1', 'Main-editor-peer review'), ('4', ' Open-peer review '), ('2', 'Single-blind peer review'), ('3', 'Double-blind peer review'), ('-1', 'Does Not state type of peer review ')], max_length=200),
        ),
    ]
