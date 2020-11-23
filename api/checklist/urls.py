from django.urls import path
from . import views

urlpatterns = [
    path('checklist/', views.TaskList.as_view()),
    path('checklist/<int:pk>/', views.TaskDetailList.as_view()),
]