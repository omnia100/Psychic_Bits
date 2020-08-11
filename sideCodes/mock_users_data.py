import sys, django, os, csv

sys.path.append(r"C:\Users\Omnia\Documents\GitHub\pbProject")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pbProject.settings")
django.setup()

from users.models import Profile
from django.contrib.auth.models import User

with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        u = User.objects.create_user(row['username'], row['email'], row['password'])
        p = Profile(user=u,score=row['score'])
        p.save()

