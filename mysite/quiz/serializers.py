from rest_framework import serializers

from .models import Question

# Define how a model class is displayed in the API response
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'