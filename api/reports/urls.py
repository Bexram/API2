from django.urls import path
from . import views


urlpatterns = [
    path('rep/', views.RepList.as_view()),
    path('rep/<int:pk>/', views.RepDetailList.as_view()),
    path('getrep/', views.GetRepList.as_view()),
    path('readyrep/', views.GetReadyRepList.as_view()),
    path('readyrep/<int:pk>/', views.ReadyRepDetail.as_view()),
    path('genreadyrep/<int:pk>/',views.PrintReadyRep.as_view()),
    path('genrep/',views.GenerateReport.as_view()),
    path('genrep/<int:pk>/',views.GenerateOneReport.as_view())
]