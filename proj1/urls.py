"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from expense import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('enterexp/',views.enterdetails),
    path('abc/',views.savedetails),
    path('calcexp1/',views.calc),
    path('exp/',views.cal1),
    path('indexp/',views.indvexp),

]
