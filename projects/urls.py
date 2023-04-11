from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects),
    path('pageTwo/<str:pk>/', views.pageTwo),
]
