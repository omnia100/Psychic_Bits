import sys, os, django
sys.path.append(r"C:\Users\Omnia\Documents\GitHub\pbProject")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pbProject.settings")
django.setup()

import csv
from PsychicBits.models import Match

with open('E0.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Match(date=row['Date'],HT=row['HomeTeam'], AT=row['AwayTeam'])
        p.save()
