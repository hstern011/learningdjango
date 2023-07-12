from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import views, response

from .models import Question
from .serializers import QuestionSerializer

class AllQuestionsView(views.APIView):
    def get(self, request):
        questions = Question.objects
        serializer = QuestionSerializer(questions, many=True)
        return response.Response(serializer.data)
    

class AnswerQuestionView(views.APIView):
    def get(self, request, question_id):
        given_answer = request.GET['answer']
        correct_answer = Question.objects.get(id=question_id).answer

        if given_answer.lower() == correct_answer.lower():
            return response.Response('Correct!')
        else:
            return response.Response('Incorrect, the correct answer is %a' % (correct_answer))