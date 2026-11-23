from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail'),
]
