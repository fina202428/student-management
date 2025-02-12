from django.urls import path
from .views import (
    UserSignupView, UserLoginView, UserLogoutView,
    StudentListCreateView, StudentDetailView,
    DepartmentListCreateView, DepartmentDetailView,
    MarksListCreateView, MarksDetailView,
    AdmissionListCreateView, AdmissionDetailView,home
)

urlpatterns = [
    path('', home, name='home'),
    path('api/auth/signup/', UserSignupView.as_view(), name='signup'),
    path('api/auth/login/', UserLoginView.as_view(), name='login'),
    path('api/auth/logout/', UserLogoutView.as_view(), name='logout'),
    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('api/departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('api/departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('api/marks/', MarksListCreateView.as_view(), name='marks-list-create'),
    path('api/marks/<int:pk>/', MarksDetailView.as_view(), name='marks-detail'),
    path('api/admissions/', AdmissionListCreateView.as_view(), name='admission-list-create'),
    path('api/admissions/<int:pk>/', AdmissionDetailView.as_view(), name='admission-detail'),
]
