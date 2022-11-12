from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from loginsta import views

urlpatterns = [
    path('', views.signin, name="signin"),
]