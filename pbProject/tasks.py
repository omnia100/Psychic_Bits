from __future__ import absolute_import, unicode_literals
from urllib.request import urlopen
from celery import shared_task
import pandas as pd



@shared_task
def Updates():
    # from API.views import predictMatchPP
    # pred = predictMatchPP('West Ham', 'Man City')
    # print(pred['draw'])
    row1, row2 = post_match_results_API()
    Update_Match_Table(row1)
    update_scores(row1['HomeTeam'], row1['HomeTeam'], row1['FTR'])

    p = Get_new_Pred(row2['HomeTeam'], row2['AwayTeam'])
    # p = 'H'
    add_pred(row2['HomeTeam'], row2['AwayTeam'], p)


def post_match_results_API():
    df = pd.read_csv('mock_results.csv', index_col=None)
    for index, row in df.iterrows():
        if row['status'] == 0:
            df.iloc[index, 6] = 1
            df.to_csv('mock_results.csv', index=False)
            return df.iloc[index], df.iloc[index+1]


def Update_Match_Table(row):
    from PsychicBits.models import Match
    m = Match.objects.filter(HT=row['HomeTeam'], AT=row['AwayTeam'])
    if m:
        m.update(FTR=row['FTR'], HT_score=row['FTHG'], AW_score=row['FTAG'])


def Get_new_Pred(h, a):
    from API.views import predict_Match
    return predict_Match(h, a)

def add_pred(home, away, pred):
    from PsychicBits.models import Match
    m = Match.objects.filter(HT=home, AT=away)
    if m:
        m.update(pred=pred)



def update_scores(home, away, result):
    from PsychicBits.models import Match
    m = Match.objects.filter(HT=home, AT=away)
    from userPrediction.views import calculateScore
    calculateScore(m,result)
