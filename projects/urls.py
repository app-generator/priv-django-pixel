from django.urls import path
from . import views

urlpatterns = [
    path('my-projects/', views.project_list, name='project_list'),
]