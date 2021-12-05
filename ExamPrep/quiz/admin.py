from django.contrib import admin
from quiz.models import Questions, Answers

class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Questions, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answers, AnswerAdmin)
