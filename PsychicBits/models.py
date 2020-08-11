from django.db import models


class Match(models.Model):
    # by default there is a MATCH.ID
    date = models.DateField()

    HT = models.CharField("Home Team", max_length=20)
    AT = models.CharField("Away Team", max_length=20)

    HT_score = models.IntegerField("Home Team Score", blank=True, default=0)
    AW_score = models.IntegerField("Away Team Score", blank=True, default=0)

    # HT_flag = models.ImageField()
    # AW_flag = models.ImageField()

    pred = models.CharField("Model Prediction", max_length=1, blank=True)
    FTR = models.CharField('Full Time Result', max_length=1, blank=True)  # H, A, D home,away,draw4

    def __str__(self):
        return '{}  vs  {}'.format(
            self.HT,
            self.AT
        )


class teamLogo(models.Model):
    team = models.CharField(max_length=20)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.team
