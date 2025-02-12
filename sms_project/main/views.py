from rest_framework import generics
from .models import User, Student, Department, Marks, Admission
from .serializers import UserSerializer, StudentSerializer, DepartmentSerializer, MarksSerializer, AdmissionSerializer
from django.http import HttpResponse

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLogoutView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class MarksListCreateView(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class MarksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class AdmissionListCreateView(generics.ListCreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class AdmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

# Other views for Student, Department, Marks, and Admission can be added similarly
def home(request):
    return HttpResponse("Welcome to the Student Management System API!")