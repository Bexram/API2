from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.AuthList.as_view()),
    path('signin/<int:pk>/', views.AuthDetailList.as_view()),
    path('getusers/', views.GetUserList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetailList.as_view()),
    path('auto/', views.AutoList.as_view()),
    path('auto/<int:pk>/', views.AutoDetailList.as_view()),
    path('getauto/<int:pk>/', views.GetAutoList.as_view()),
    path('units/', views.UnitList.as_view()),
    path('units/<int:pk>/', views.UnitDetailList.as_view()),
]