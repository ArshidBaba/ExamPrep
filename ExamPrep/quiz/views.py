import imp
from rest_framework import generics
from .models import Questions
from .serializers import QuestionSerializer
from rest_framework.views import APIView

class Question(generics.ListAPIView):

    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()

# class RandomQuestion(APIView):

#     def get(self, request, format:None, **kwargs):
#         question = Question.objects.filter(qu


