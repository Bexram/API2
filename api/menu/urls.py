from .views import MenuList
from django.urls import path

urlpatterns = [
    path('', MenuList.as_view()),

]
