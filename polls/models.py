from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Applicator(models.Model):
    name = models.CharField(max_length=200, default="")
    info = models.TextField()
    avatar_url = models.CharField(default="", max_length=255)
    user = models.ForeignKey(User)
    region = models.IntegerField(default=-1)

    def __str__(self):
        return self.name + " " + self.avatar_url


class Skill(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    applicators = models.ManyToManyField(Applicator, through='ApplicatorSkill')

    def __str__(self):
        return self.name

class ApplicatorSkill(models.Model):
    applicator = models.ForeignKey(Applicator)
    skill = models.ForeignKey(Skill)
    skill_level = models.IntegerField(default=0)

    def __str__(self):
        return self.applicator + " " + self.skill


class Company(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    company = models.ForeignKey(Company)
    region = models.IntegerField()
    skills = models.ManyToManyField(Skill, through='VacancySkill')

    def __str__(self):
        return self.title

class VacancySkill(models.Model):
    skill = models.ForeignKey(Skill)
    vacancy = models.ForeignKey(Vacancy)
    necessary_level = models.IntegerField(default=0)

    def __str__(self):
        return self.vacancy + " " + self.skill