from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('questions/post_question/', views.post_question, name='post_question'),
    path('questions/details/<slug:slug>/', views.question_details, name='question_details'),
    path('questions/post_answer/<slug:slug>/', views.post_answer, name='post_answer'),
    path('questions/update/<slug:slug>/', views.update_question, name='update_question'),
    path('questions/delete/<slug:slug>/', views.delete_question, name='delete_question'),
    path('questions/upvotes/<slug:slug>/', views.question_upvotes, name='question_upvotes'),

]