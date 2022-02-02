from re import I
from rest_framework import serializers
from .models import Questions

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ['title',]