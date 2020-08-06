# Generated by Django 2.2.14 on 2020-08-06 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PsychicBits', '0002_teamlogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(max_length=5)),
                ('matchID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PsychicBits.Match')),
            ],
        ),
    ]
