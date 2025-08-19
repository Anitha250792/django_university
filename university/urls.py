from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, DepartmentViewSet, CourseViewSet

router = DefaultRouter()
router.register('universities', UniversityViewSet, basename='university')
router.register('departments', DepartmentViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
