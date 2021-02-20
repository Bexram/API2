from django.urls import path
from . import views


urlpatterns = [
    path('rep/', views.Report.as_view()),
]