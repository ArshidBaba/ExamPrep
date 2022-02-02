from django.urls import path
from .views import Question

app_name= 'quiz'

urlpatterns = [
    path('', Question.as_view(), name='quiz'),
]