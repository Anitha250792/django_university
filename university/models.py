from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    university = models.ForeignKey(University, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
