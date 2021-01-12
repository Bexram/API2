from django.urls import path
from . import views

urlpatterns = [
    path('vacations/', views.VacationList.as_view()),
    path('getallvacations/', views.VacationGetAllList.as_view()),
    path('getvacation/', views.VacationGetList.as_view()),
    path('vacations/<int:pk>/', views.VacationDetail.as_view()),

]
