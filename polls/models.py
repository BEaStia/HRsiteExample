from django.db import models

# Create your models here.

class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=200,default="")
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField(auto_now=True,auto_now_add=True)

class Application(models.Model):
	name = models.CharField(max_length=200,default="")
	info = models.TextField()
	avatar_url = models.FilePathField()
	user = models.ForeignKey('User')
	
class Skill(models.Model):
	name = models.CharField(max_length=200)
	info = models.TextField()
	applications = models.ManyToMany(Application, through='ApplicationSkill')

class ApplicationSkill(models.Model):
	application_id = models.ForeignKey(Application)
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
	region = models.IntegerKey()
	skills = models.ManyToManyField(Skill, through='VacancySkill')

class VacancySkill(models.Model):
	skill = models.Foreignkey(Skill)
	vacancy = models.ForeignKey(Vacancy)
	necessary_level = models.IntegerField(default = 0) 
