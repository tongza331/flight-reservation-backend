"""flight URL Configuration

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
from flightapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path("register", views.register_request, name="register"),
    path("flight", views.login_request, name="flight"),
    path("logout",views.logout,name='logout'),
    path("flight/search",views.search,name='search'),
    path("new/flight/search",views.new_search,name='new_search'),
    path("flight/review/one_way",views.review,name='review'),
    path("flight/review/round_trip",views.review2,name='review2'),
]
