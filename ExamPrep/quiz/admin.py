from django.contrib import admin
from . import models

class AnswerAdmin(admin.TabularInline):
    model = models.Answers
# admin.site.register(models.Answers, AnswerAdmin)  

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerAdmin,
    ]
admin.site.register(models.Questions, QuestionAdmin)


