"""
URL configuration for enrollmentsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# your_app/urls.py
from django.urls import path
from enrollment .views import (
    StudentListCreateView, StudentRetrieveUpdateDestroyView,
    CourseListCreateView, CourseRetrieveUpdateDestroyView,
    LecturerListCreateView, LecturerRetrieveUpdateDestroyView,
    EnrollmentListCreateView, EnrollmentRetrieveUpdateDestroyView,
    GradeListCreateView, GradeRetrieveUpdateDestroyView
)

urlpatterns = [
    # Student URLs
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),

    # Course URLs
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),

    # Lecturer URLs
    path('lecturers/', LecturerListCreateView.as_view(), name='lecturer-list-create'),
    path('lecturers/<int:pk>/', LecturerRetrieveUpdateDestroyView.as_view(), name='lecturer-detail'),

    # Enrollment URLs
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-detail'),

    # Grade URLs
    path('grades/', GradeListCreateView.as_view(), name='grade-list-create'),
    path('grades/<int:pk>/', GradeRetrieveUpdateDestroyView.as_view(), name='grade-detail'),
]
