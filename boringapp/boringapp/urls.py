"""boringapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

if settings.DEBUG==True:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',views.homepage,name='homepage'),
        path('blogpost/<int:article_id>/',views.blogpost,name='blogpost')
    ]
    urlpatterns += staticfiles_urlpatterns()
else:
    urlpatterns = [
        path('',views.homepage,name='homepage'),
        path('blogpost/<int:article_id>/',views.blogpost,name='blogpost')
    ]
    urlpatterns += staticfiles_urlpatterns()
