from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('<slug:slug>/', views.prodDetail, name="prodDetail"),
]
