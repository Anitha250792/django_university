from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import University, Department, Course
from .serializers import UniversitySerializer, DepartmentSerializer, CourseSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    # Nested endpoint for departments
    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        university = self.get_object()
        departments = university.departments.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
