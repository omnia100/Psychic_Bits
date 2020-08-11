# Generated by Django 3.1 on 2020-08-11 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PsychicBits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(max_length=1)),
                ('matchID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PsychicBits.match')),
            ],
        ),
    ]
