from django.urls import path
from . import views

urlpatterns = [
    path('getchecklist/', views.TaskGetList.as_view()),
    path('checklist/', views.TaskList.as_view()),
    path('checklist/<int:pk>/', views.TaskDetailList.as_view()),
    path('addyear/', views.TaskAddYear.as_view()),
    path('deleteyear/<int:year>/', views.TaskDeleteYear.as_view()),
]