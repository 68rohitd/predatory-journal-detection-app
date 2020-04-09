from django.db import models

class Meta:
    abstract = True

class Journaltable(models.Model):
    predatory = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    topic = models.CharField(max_length = 200)
    domain = models.CharField(max_length = 200) 
    journal = models.CharField(max_length = 200)

    Metric = (
        # email
            (   
                ('Email_of_Editor', '-----'),
                ('2', 'Official'),
                ('1', 'general Email Service'),
                ('0', 'Not Available')
            ),
        #affiliation 
            (   
                ('Affiliation_of_Editor', '-----'),
                ('2', 'Full affiliation'),
                ('1', 'Only country name'),
                ('0', 'Not Available')
            ),
        # bogus metric or indexx
            (   
                ('Using_bogus_metric_and_index', '-----'),
                ('1', 'No'),
                ('0', 'Yes')
            ),
        # no of editors
            (   
                ('Number_of_Editors', '-----'),
                ('2', 'More than 7'),
                ('1', 'Between 5-7'),
                ('0', 'Lower than 5')
            ),
        # Review time 
            (   
                ('Review_Time', '-----'),
                ('2', 'More than a month'),
                ('1', 'Lower than a month'),
                ('0', 'Lower than a week')
            )
    )
    Email_of_Editor = models.CharField(max_length=200, choices = Metric[0])
    Affiliation_of_Editor = models.CharField(max_length=200, choices = Metric[1])
    Using_bogus_metric_and_index = models.CharField(max_length=200, choices = Metric[2])
    Number_of_Editors = models.CharField(max_length=200, choices = Metric[3])
    Review_Time = models.CharField(max_length=200, choices = Metric[4])

    
    # Unclear_Review_Process = models.BooleanField(default=False)
    # Number_of_Paper_in_each_issue = models.BooleanField(default=False)
    # Questionable_special_issue = models.BooleanField(default=False)
    # Availablity_of_Journal_Full_Address = models.BooleanField(default=False)
    # Using_bogus_metric_and_index = models.BooleanField(default=False)
    # Send_journal_spam_Email_to_recieve_papers = models.BooleanField(default=False)
    # Fastrack_Fee = models.BooleanField(default=False)
    # Submission_Fee = models.BooleanField(default=False)
    # Publication_Fee = models.BooleanField(default=False)
    # Charging_both_authors_and_readers = models.BooleanField(default=False)
    # Defined_aim_and_scope = models.BooleanField(default=False)
    # Journal_relevance = models.BooleanField(default=False)
    # Errorenous_journal = models.BooleanField(default=False)
    # Necessary_info = models.BooleanField(default=False)
    # Transperancy = models.BooleanField(default=False)
    # Listed_in_doaj = models.BooleanField(default=False)

    def __str__(self):
        return "publisher {0} topic {1} domain {2} journal {3} Email_of_Editor {4} Affiliation_of_Editor {5} Using_bogus_metric_and_index{6} Number_of_Editors {7} Review_Time{8}".format(self.publisher, self.topic, self.domain, self.journal, self.Email_of_Editor, self.Affiliation_of_Editor,self.Using_bogus_metric_and_index, self.Number_of_Editors, self.Review_Time)

#creating new table  
class Journaltable2(models.Model):

    Metric = (
            (   
                ('Old_new', '-----'),
                ('1', 'Old'),
                ('0', 'New'),
            ),
            (   
                ('email_of_editor', '-----'),
                ('-1', ' Not available'),
                ('1', 'General email service'),
                ('2', 'Official email'),
            ),
            (  
                ('impact_factor', '-----'),
                ('-2', 'Not available (if it’s an old journal)'),
                ('1', '0-1.5'),
                ('2', '1.5-3'),
                ('3', '3-4.5'),
                ('4', '4.5-6'),
                ('-1', 'None of these'),
            ),
            (  
                ('number_of_editors', '-----'),
                ('0', 'Lower than 5'),
                ('1', 'Between 5-7'),
                ('2', 'More than 7'),
                ('-1', 'Doesn’t mention'),
            ),
            (  
                ('review_time', '-----'),
                ('-1', 'Lower than a week'),
                ('1', 'Lower than a month'),
                ('2', 'More than a month'),
                ('-2', ' Doesn’t mention '),
            ),
            (  
                ('review_process', '-----'),
                ('2', ' The journal states whether it is peer reviewed/edited and has a review policy listed.'),
                ('1', '  The journal states whether it is peer reviewed/edited and has no review policy listed '),
                ('-1', ' The journal does not state whether it is peer reviewed/edited and has no review policy listed.'),
            ),
            (  
                ('journal_website', '-----'),
                ('3', ' The journal website is competently designed and functional. (examples: no broken links, easy navigation, no missing information)'),
                ('2', '  The journal website is adequately designed with passable functionality        . (examples: adequate navigation, few broken links, some missing information) '),
                ('1', ' The journal is poorly designed and is not functional. (examples: broken links, poor navigation, missing information)'),
            ),
            (  
                ('fast_track_fee', '-----'),
                ('-1', ' Very High fast track fee'),
                ('1', '  Reasonable fee '),
                ('2', ' No Fee'),
                ('-2', ' doesnt mention'),
            ),
            (  
                ('author_fee_for_subscription_model', '-----'),
                ('-1', 'The author is charged for publishing'),
                ('1', '  The author is not charged for publishing  '),
                ('0', ' It is not subscription model'),
            ),
            (  
                ('author_fee_for_open_access', '-----'),
                ('2', 'The journal clearly states the amount of money an author will pay to have each article published'),
                ('1', 'The journal states that an author fee is required but does not note how much it is.'),
                ('-1', 'The journal does not state whether or not there are any author fees'),
                ('0', 'Not open access model '),
            ),
            (  
                ('charging_for_readers_for_open_access', '-----'),
                ('-1', 'The reader is charged for reading'),
                ('0', 'The reader is not charge for reading/ it is not open access'),
            ),
            (  
                ('journal_name', '-----'),
                ('2', 'Name not confused with another journal '),
                ('1', 'The journal has a name similar to another journal but is able to be distinguished between the two.'),
                ('-1', 'The journal is unable to be distinguished from another with a similar name'),
            ),
            (  
                ('conflicts_of_interest', '-----'),
                ('2', 'The journal thoroughly and clearly states a conflicts of interest policy, including how it will handle potential conflicts of interest of editors, authors, and reviewers'),
                ('1', 'The journal states a conflicts of interest policy, but the description of how conflicts will be handled is unclear'),
                ('-1', 'The journal does not state a conflicts of interest policy'),
            ),
            (  
                ('revenue_sources', '-----'),
                ('2', 'The journal clearly states its business model. This includes any revenue sources, like author fees, subscriptions, advertising, reprints, institutional support, and organizational support'),
                ('1', 'The journal\'s business model lacks clarity when stating its revenue sources, like author fees, subscriptions, advertising, reprints, institutional support, and organizational support '),
                ('-1', ' The journal does not state its business model'),
            ),
            (  
                ('journal_archive', '-----'),
                ('2', 'The journal website contains an archive of its past issues with links to full text articles'),
                ('1', 'The journal website contains an archive but it may be incomplete or does not contain links to full text articles '),
                ('0', ' The journal does not have an archive of its past issues (new Journal )'),
                ('-1', ' The journal does not have an archive of its past issues (old Journal)'),
            ),
            (  
                ('publishing_schedule', '-----'),
                ('2', 'The journal clearly states how often its issues will be published each year and this agrees with the archive'),
                ('1', ' The journal does not state how often its issues will be published but it can be determined from the archive'),
                ('-1', 'The journal does not state how often its issues will be published each year and it cannot be determined from the archive ')
            ),
            (  
                ('copyright_info', '-----'),
                ('1', 'The journal clearly describes its copyright and licensing information on the journal\'s Web site, and licensing terms are indicated on the published articles (HTML/PDF)'),
                ('-1', ' Copyright and licensing information is not found on the journal\'s Web site and on any published article'),
            ),
            (  
                ('journal_index', '-----'),
                ('2', 'The journal is indexed in more than one subject database. (examples: ERIC, Google Scholar, Web of Science, PsycINFO) '),
                ('1', '  The journal is indexed in one subject database. (example: ERIC) '),
                ('-1', '  The journal is not indexed in a subject database')
            ),
            (  
                ('publisher_info', '-----'),
                ('1', ' Information about the ownership/management of the journal and contact information about the publisher is clearly identified'),
                ('-1', '   Information about the ownership/management of the journal and contact information about the publisher is not availabl')
            ),
            (  
                ('type_of_peer_review', '-----'),
                ('-2', ' No-peer-review'),
                ('1', 'Main-editor-peer review'),
                ('4', ' Open-peer review '),
                ('2', 'Single-blind peer review'),
                ('3', 'Double-blind peer review'),
                ('-1', 'Does Not state type of peer review ')
            ),
            (  
                ('clarity_of_abstract_Internation_Journal', '-----'),
                ('-2', 'No abstract'),
                ('-1', 'Abstract non-English '),
                ('1', 'Abstract in English fairly clear '),
                ('2', 'Abstract in English very clear')
            ),
            (  
                ('clarity_of_abstract_Regional_Journal', '-----'),
                ('-2', 'No abstract'),
                ('-1', 'Abstract in Non Regional Language'),
                ('1', 'Abstract in Regional Language, fairly clear'),
                ('2', 'Abstract in Regional Language, very clear'),
                ('0', 'Not a regional journal'),
            ),
            (  
                ('quality_of_and_comformity_with_stated_aim', '-----'),
                ('1', ' Based on abstract, topic is covered clearly'),
                ('-1', 'Based on abstract, topic is not covered clearly '),
                ('-2', 'Based on abstract,  journal is not relevant')
            ),
            (  
                ('readability_of_article', '-----'),
                ('-1', 'Extremely Poor in sentence formation, Word usage, sentence beginnings and many grammatical mistakes '),
                ('1', 'Fairly good in sentence formation, Word usage, sentence beginnings and few  to none grammatical/spelling mistakes '),
                ('2', 'Excellent in sentence formation, Word usage, sentence beginnings and no grammatical mistakes'),
            ),
            (  
                ('content_availability', '-----'),
                ('-1', 'Recent content available online'),
                ('0', 'Recent content not available online')
            ),
            (  
                ('english_language_homepage_availability_International_journal', '-----'),
                ('-2', 'not in eng'),
                ('-1', 'partially in eng'),
                ('1', 'entirely in eng')
            ),
            (  
                ('regional_language_homepage_availability_Regional_journal', '-----'),
                ('-2', 'not in reg lang'),
                ('-1', 'partially in reg lng'),
                ('1', 'entirely in reg lang'),
                ('0', 'journal not regional'),
            ),
            (  
                ('If_open_access_is_it_listed_in_directory_of_open_access_journal', '-----'),
                ('1', 'yes'),
                ('-1', 'no')
            ),
            (  
                ('affiliation_of_editors', '-----'),
                ('1', 'full afflle'),
                ('-1', 'no affl avai')
            ),
            (  
                ('diversity_in_geographical_distribution_of_editors', '-----'),
                ('-2', 'No editorial board '),
                ('-1', 'Regional diversity of editorial board is not in line with editorial concept'),
                ('1', 'Regional diversity of editorial board is partially in line with editorial concept'),
                ('2', 'Regional diversity of editorial board is entirely in line with editorial concept')
            ),
            (  
                ('diversity_in_geographical_distribution_of_authors', '-----'),
                ('-1', 'Regional diversity of authors board is not in line with editorial concept'),
                ('1', 'Regional diversity of authors board is partially in line with editorial concept'),
                ('2', 'Regional diversity of authors board is entirely in line with editorial concept')
            ),
            (  
                ('plagiarism', '-----'),
                ('2', '0% - 5\% '),
                ('1', '5% - 10\%'),
                ('-1', '10% - 50\%'),
                ('-2', 'beyond 50\%'),
                ('0', ' not mentin')
            ),
            (  
                ('similarity_of_website_design', '-----'),
                ('-1', 'Similar to other Website Designs'),
                ('1', 'uniqye Website Design'),
            ),
            (  
                ('editors_standing', '-----'),
                ('-2', 'extremely poor'),
                ('-1', ' poor'),
                ('0', 'fair'),
                ('1', 'good'),
                ('2', 'extreely god'),
            ),
            (  
                ('convincing_editorial_scope', '-----'),
                ('-2', 'not conv'),
                ('-1', ' poor'),
                ('0', 'fair'),
                ('1', 'good'),
                ('2', 'extreely god'),
            ),
            (  
                ('send_jornal_spam_email_to_review_papers', '-----'),
                ('-1', 'yes'),
                ('0', 'no'),
            ),
            (  
                ('questionable_special_issue', '-----'),
                ('1', 'yes'),
                ('0', 'no'),
            ),
            (  
                ('Predatory_1_Non_predatory_0', '-----'),
                ('1', 'yes'),
                ('0', 'no'),
            ),
    )

    Name_of_journal = models.CharField(max_length = 200)
    Links = models.CharField(max_length = 200)
    Category = models.CharField(max_length = 200)	
    
    Old_new	= models.CharField(max_length = 200, choices = Metric[0])
    email_of_editor = models.CharField(max_length = 200, choices = Metric[1])
    impact_factor = models.CharField(max_length = 200, choices = Metric[2])
    number_of_editors = models.CharField(max_length = 200, choices = Metric[3])	
    review_time = models.CharField(max_length = 200, choices = Metric[4])	
    review_process = models.CharField(max_length = 200, choices = Metric[5])	
    journal_website = models.CharField(max_length = 200, choices = Metric[6])	
    fast_track_fee = models.CharField(max_length = 200, choices = Metric[7])	
    author_fee_for_subscription_model = models.CharField(max_length = 200, choices = Metric[8])	
    author_fee_for_open_access = models.CharField(max_length = 200, choices = Metric[9])	
    charging_for_readers_for_open_access = models.CharField(max_length = 200, choices = Metric[10])	
    journal_name = models.CharField(max_length = 200, choices = Metric[11])	
    conflicts_of_interest = models.CharField(max_length = 200, choices = Metric[12])	
    revenue_sources = models.CharField(max_length = 200, choices = Metric[13])	
    journal_archive = models.CharField(max_length = 200, choices = Metric[14])	
    publishing_schedule = models.CharField(max_length = 200, choices = Metric[15])	
    copyright_info = models.CharField(max_length = 200, choices = Metric[16])	
    journal_index = models.CharField(max_length = 200, choices = Metric[17])	
    publisher_info = models.CharField(max_length = 200, choices = Metric[18])	
    type_of_peer_review = models.CharField(max_length = 200, choices = Metric[19])	
    clarity_of_abstract_Internation_Journal = models.CharField(max_length = 200, choices = Metric[20])	
    clarity_of_abstract_Regional_Journal = models.CharField(max_length = 200, choices = Metric[21])	
    quality_of_and_comformity_with_stated_aim = models.CharField(max_length = 200, choices = Metric[22])	
    readability_of_article = models.CharField(max_length = 200, choices = Metric[23])	
    content_availability = models.CharField(max_length = 200, choices = Metric[24])	
    english_language_homepage_availability_International_journal = models.CharField(max_length = 200, choices = Metric[25])	
    regional_language_homepage_availability_Regional_journal = models.CharField(max_length = 200, choices = Metric[26])	
    If_open_access_is_it_listed_in_directory_of_open_access_journal = models.CharField(max_length = 200, choices = Metric[27])	
    affiliation_of_editors = models.CharField(max_length = 200, choices = Metric[28])	
    diversity_in_geographical_distribution_of_editors = models.CharField(max_length = 200, choices = Metric[29])	
    diversity_in_geographical_distribution_of_authors = models.CharField(max_length = 200, choices = Metric[30])	
    plagiarism = models.CharField(max_length = 200, choices = Metric[31])	
    similarity_of_website_design = models.CharField(max_length = 200, choices = Metric[32])	
    editors_standing = models.CharField(max_length = 200, choices = Metric[33])	
    convincing_editorial_scope = models.CharField(max_length = 200, choices = Metric[34])	
    send_jornal_spam_email_to_review_papers = models.CharField(max_length = 200, choices = Metric[35])	
    questionable_special_issue = models.CharField(max_length = 200, choices = Metric[36])	
    Predatory_1_Non_predatory_0 = models.CharField(max_length = 200, choices = Metric[37])