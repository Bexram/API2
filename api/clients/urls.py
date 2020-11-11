from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetailList.as_view()),
    path('objects/', views.ObjectList.as_view()),
    path('objects/<int:pk>/', views.ObjectDetailList.as_view()),
    path('contactman/', views.ContactManList.as_view()),
    path('contactman/<int:pk>/', views.ContactManDetailList.as_view()),
    path('contract/', views.ContractList.as_view()),
    path('contract/<int:pk>/', views.ContractDetailList.as_view()),
]