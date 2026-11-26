from django.urls import path
from . import views

urlpatterns = [
    path('', views.college_home, name='college_home'),
    path('university/<int:pk>/', views.university_detail, name='university_detail'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('semester/<int:pk>/', views.semester_detail, name='semester_detail'),
    path('college-subject/<int:pk>/chapters/', views.college_subject_chapters, name='college_subject_chapters'),
    path('college-subject/<int:pk>/papers/', views.college_subject_papers, name='college_subject_papers'),
    path('college-chapter/<int:pk>/', views.college_chapter_detail, name='college_chapter_detail'),

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    path('api/universities/', views.api_universities, name='api_universities'),
    path('api/universities/<int:pk>/courses/', views.api_courses, name='api_courses'),
    path('api/courses/<int:pk>/semesters/', views.api_semesters, name='api_semesters'),
    path('api/semesters/<int:pk>/subjects/', views.api_college_subjects, name='api_college_subjects'),
    path('api/subjects/<int:pk>/documents/', views.api_college_documents, name='api_college_documents'),

]