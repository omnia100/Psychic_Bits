import sys, os, django
sys.path.append(r"C:\Users\AIDa_MAhmoud\Documents\GitHub\Psychic_Bits")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pbProject.settings")
django.setup()

import csv
from API.models import matchData

with open('features.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = matchData(HomeTeam=row['Home Team'], AwayTeam=row['Away Team'], Referee=row['Referee'],
                      AttackRateH=row['AttackRateH'], AttackRateA=row['AttackRateA'], DefenceRateH=row['DefenceRateH'],
                      DefenceRateA=row['DefenceRateA'], DGH=row['DGH'], DGA=row['DGA'], HomeRank=row['Home Rank'],
                      AwayRank=row['Away Rank'], AvgHST=row['Avg HST'], AvgAST=row['Avg AST'], AvgHF=row['Avg HF'],
                      AvgAF=row['Avg AF'], AvgHC=row['Avg HC'], AvgAC=row['Avg AC'], AvgHR=row['Avg HR'],
                      AvgAR=row['Avg AR'], AvgHY=row['Avg HY'], AvgAY=row['Avg AY'])
        p.save()