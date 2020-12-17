from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('getalltasks/', views.TaskGetAllList.as_view()),
    path('gettasks/', views.TaskGetList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('getstasks/<int:pk>/', views.GetSTaskList.as_view()),
    path('stasks/', views.STaskList.as_view()),
    path('stasks/<int:pk>/', views.STaskDetailList.as_view()),
    path('getfoto/<int:pk>/', views.GetFoto.as_view()),
    path('foto/', views.SFotoTaskList.as_view()),
    path('foto/<int:pk>/', views.STaskDetailList.as_view()),
]
