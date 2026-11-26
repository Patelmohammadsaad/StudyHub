from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    path('chapter/<int:pk>/', views.chapter_detail, name='chapter_detail'),
    path('school/', views.school_page, name='school_page'),
    path('subject/<int:pk>/chapters/', views.subject_chapters, name='subject_chapters'),
    path('subject/<int:pk>/papers/', views.subject_papers, name='subject_papers'),

    
    # //////////////////////////////////////////////////////////////////////////////
    path('api/classes/', views.api_classes, name='api_classes'),
    path('api/classes/<int:pk>/subjects/', views.api_subjects, name='api_subjects'),
    path('api/subjects/<int:pk>/documents/', views.api_documents, name='api_documents'),
    path('api/subjects/<int:pk>/chapters/', views.api_chapters, name='api_chapters'),
    path('api/subjects/<int:pk>/papers/', views.api_papers, name='api_papers'),
    path('api/chapters/<int:pk>/documents/', views.api_chapter_documents, name='api_chapter_documents'),
]
    