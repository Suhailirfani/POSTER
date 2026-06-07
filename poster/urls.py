from django.urls import path
from . import views

app_name = 'poster'

urlpatterns = [
    path('', views.home, name='home'),
    path('program/new/', views.create_program, name='create_program'),
    path('program/<int:pk>/', views.program_detail, name='program_detail'),
    path('program/<int:pk>/preview/', views.preview, name='preview'),
    path('program/<int:pk>/edit/', views.edit_program, name='edit_program'),
    path('program/<int:pk>/delete/', views.delete_program, name='delete_program'),
]
