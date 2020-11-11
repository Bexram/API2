from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.AuthList.as_view()),
    path('signin/<int:pk>/', views.AuthDetailList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetailList.as_view()),
]