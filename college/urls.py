from django.urls import path
from . import views

urlpatterns = [
    path('', views.college_home, name='college_home'),
    path('university/<int:pk>/', views.university_detail, name='university_detail'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('subject/<int:pk>/books/', views.course_books, name='course_books'),
    path('subject/<int:pk>/papers/', views.course_papers, name='course_papers'),
    path('subject/<int:pk>/notes/', views.course_notes, name='course_notes'),

    # //////////////////////////////////////////////////////////////////////////////
    path('api/universities/', views.api_universities, name='api_universities'),
    path('api/universities/<int:pk>/courses/', views.api_courses, name='api_courses'),
    path('api/courses/<int:pk>/books/', views.api_books, name='api_books'),
    path('api/courses/<int:pk>/papers/', views.api_papers, name='api_papers'),
]