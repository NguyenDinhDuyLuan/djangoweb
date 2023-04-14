from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('pageTwo/<str:pk>/', views.pageTwo, name="project"),
]
