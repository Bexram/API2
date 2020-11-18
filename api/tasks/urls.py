from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/', views.TaskGetList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('stasks/', views.STaskList.as_view()),
    path('stasks/<int:pk>/', views.STaskDetailList.as_view()),
]