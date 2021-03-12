from django.urls import path
from . import views

urlpatterns = [
    path('allowance/', views.AllowanceList.as_view()),
    path('allowance/<int:pk>/', views.AllowanceDetailList.as_view()),
    path('getallowance/', views.GetAllowanceList.as_view()),
    path('getallowance/<int:pk>/', views.GetAllowanceList.as_view()),
    path('verifications/', views.VerificationsList.as_view()),
    path('verifications/<int:pk>/', views.VerificationsDetailList.as_view()),
    path('insurance/', views.InsuranceList.as_view()),
    path('insurance/<int:pk>/', views.InsuranceDetailList.as_view()),
    path('getinsurance/', views.GetInsuranceList.as_view()),
]