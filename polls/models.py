from django.db import models


class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=200,default="")
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField(auto_now=True)

class Applicator(models.Model):
	name = models.CharField(max_length=200,default="")
	info = models.TextField()
	avatar_url = models.FilePathField()
	user = models.ForeignKey('User')
	
class Skill(models.Model):
	name = models.CharField(max_length=200)
	info = models.TextField()
	applicators = models.ManyToManyField(Applicator, through='ApplicatorSkill')

class ApplicatorSkill(models.Model):
	applicator_id = models.ForeignKey(Applicator)
	skill = models.ForeignKey(Skill)
	skill_level = models.IntegerField(default = 0)

class Company(models.Model):
	name = models.CharField(max_length=200)
	info = models.TextField()
	user = models.ForeignKey(User)

class Vacancy(models.Model):
	title = models.CharField(max_length=200)
	info = models.TextField()
	company = models.ForeignKey(Company)
	region = models.IntegerField()
	skills = models.ManyToManyField(Skill, through='VacancySkill')

class VacancySkill(models.Model):
	skill = models.ForeignKey(Skill)
	vacancy = models.ForeignKey(Vacancy)
	necessary_level = models.IntegerField(default = 0) 
