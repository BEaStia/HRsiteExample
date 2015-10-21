# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('info', models.TextField()),
                ('avatar_url', models.CharField(default=b'', max_length=255)),
                ('region', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicatorSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_level', models.IntegerField(default=0)),
                ('applicator', models.ForeignKey(to='polls.Applicator')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('applicators', models.ManyToManyField(to='polls.Applicator', through='polls.ApplicatorSkill')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default=b'', max_length=200)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('region', models.IntegerField()),
                ('company', models.ForeignKey(to='polls.Company')),
            ],
        ),
        migrations.CreateModel(
            name='VacancySkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('necessary_level', models.IntegerField(default=0)),
                ('skill', models.ForeignKey(to='polls.Skill')),
                ('vacancy', models.ForeignKey(to='polls.Vacancy')),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(to='polls.Skill', through='polls.VacancySkill'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(to='polls.User'),
        ),
        migrations.AddField(
            model_name='applicatorskill',
            name='skill',
            field=models.ForeignKey(to='polls.Skill'),
        ),
        migrations.AddField(
            model_name='applicator',
            name='user',
            field=models.ForeignKey(to='polls.User'),
        ),
    ]
