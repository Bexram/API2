from django.urls import path
from . import views

urlpatterns = [
    path('getcompany/', views.CompanyGetList.as_view()),
    path('getchecklist/<int:pk>/', views.TaskGetList.as_view()),
    path('checklist/', views.TaskList.as_view()),
    path('checklist/<int:pk>/', views.TaskDetailList.as_view()),
]