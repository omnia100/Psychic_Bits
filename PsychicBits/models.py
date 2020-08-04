from django.db import models

#
# class User(models.Model):
#     email = models.EmailField(max_length=254)
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=50)
#     # ToDo : see how to hash and manage passwords
#     # ToDo : see modelforms
#     # picture = models.ImageField() ##Avatar as default
#     # favTeam = models.CharField(blank=True,max_length=10,choice = ) #from Team table?
#     # votes (one u to many v)
#
#
# class Vote(models.Model):
#


class Match(models.Model):
    # by default there is a MATCH.ID
    date = models.DateField()

    HT = models.CharField("Home Team", max_length=20)
    AT = models.CharField("Away Team", max_length=20)

    # HT_score = models.IntegerField("Home Team Score", max_length=2, blank=True)
    # AW_score = models.IntegerField("Away Team Score", max_length=2, blank=True)

    # HT_flag = models.ImageField()
    # AW_flag = models.ImageField()

    pred = models.CharField("Model Prediction",max_length=1, blank=True)
    FTR = models.CharField('Full Time Result',max_length=1, blank=True) # H, A, D home,away,draw


