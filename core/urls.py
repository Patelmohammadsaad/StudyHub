from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    path('school/', views.school_page, name='school_page'),
    path('subject/<int:pk>/papers/', views.subject_papers, name='subject_papers'),
    path('subject/<int:pk>/books/', views.subject_books, name='subject_books'),
    path('subject/<int:pk>/notes/', views.subject_notes, name='subject_notes'),

    # //////////////////////////////////////////////////////////////////////////////
    path('api/classes/', views.api_classes, name='api_classes'),
    path('api/classes/<int:pk>/subjects/', views.api_subjects, name='api_subjects'),
    path('api/subjects/<int:pk>/papers/', views.api_papers, name='api_papers'),
    ]