from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    age = models.IntegerField()
    is_active = models.BooleanField(default=False)

