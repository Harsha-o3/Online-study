#course/models.py
from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
        