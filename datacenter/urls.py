"""datacenter URL Configuration

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
from mysite import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('date/', views.date),
    path('lotto/', views.lotto),
    path('', views.index),
    path('mom/', views.mom),
    path('passfirst/', views.passfirst),
    path('passsecond/', views.passsecond),
    path('passthird/', views.passthird),
    path('passfourth/', views.passfourth),
    path('play/', views.play ),
    path('play1/', views.play1 ),
    path('play2/', views.play2 ),
    path('play3/', views.play3 ),
    path('play4/', views.play4 ),
    path('play5/', views.play5 )
]
