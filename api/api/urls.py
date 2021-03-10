import os

from django.contrib.auth import views as authviews
from django import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import settings
from django.conf.urls.static import static

"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="CUBR API",
        default_version='v1',
        description="API для Владосика! Смотри сюда, пржеде чем меня спросить!!!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('password_reset/',authviews.PasswordResetView.as_view(success_url='http://cubp.szsb.ru:8080',
         extra_email_context={'company_name':'CUBP'},
         email_template_name=os.path.abspath('templates/reset_email.html'),
         subject_template_name=os.path.abspath('templates/reset_subject.txt'))),
    path('password_reset/done/', authviews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authviews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', urls.include('reports.urls')),
    path('', urls.include('users.urls')),
    path('', urls.include('allowance.urls')),
    path('', urls.include('clients.urls')),
    path('', urls.include('tasks.urls')),
    path('', urls.include('checklist.urls')),
    path('', urls.include('vacations.urls')),
    path('menu/', urls.include('menu.urls')),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)