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
    # metrics
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