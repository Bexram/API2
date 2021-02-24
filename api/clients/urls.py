
from django.urls import path
from . import views


urlpatterns = [
    path('getclients/', views.ClientGetList.as_view()),
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetailList.as_view()),
    path('objects/', views.ObjectList.as_view()),
    path('objects/<int:pk>/', views.ObjectDetailList.as_view()),
    path('getcontactman/<int:pk>/', views.GetContactManList.as_view()),
    path('contactman/', views.ContactManList.as_view()),
    path('contactman/<int:pk>/', views.ContactManDetailList.as_view()),
    path('contract/', views.ContractList.as_view()),
    path('contract/<int:pk>/', views.ContractDetailList.as_view()),
    path('getobjects/<int:pk>/', views.GetObjectList.as_view()),
    path('getcontracts/<int:pk>/', views.GetContractList.as_view()),

]
