from django.contrib import admin


from .models import Company, User, Vacancy, Skill, Applicator

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Vacancy)
admin.site.register(Skill)
admin.site.register(Applicator)

# Register your models here.
