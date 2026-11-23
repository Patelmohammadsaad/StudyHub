from django.urls import path
from . import views

urlpatterns = [
    path('', views.college_home, name='college_home'),
    path('university/<int:pk>/', views.university_detail, name='university_detail'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('semester/<int:pk>/', views.semester_detail, name='semester_detail'),
    path('college-subject/<int:pk>/', views.college_subject_detail, name='college_subject_detail'),

]
