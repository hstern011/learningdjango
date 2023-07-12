from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.AllQuestionsView.as_view(), name='index'),
    path('<int:question_id>/', views.AnswerQuestionView.as_view())
]
