"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from polls_angular.views import logout, Index

urlpatterns = [
    url(r"^$", Index.as_view(), name="index"),
    url(r"logout/$", logout, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('polls_angular/', include('polls_angular.urls')),
    path('admin/', admin.site.urls),
    url(r"^api/", include("api.urls"), name="api"),
]
