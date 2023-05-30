from django.db import models
from .utils import *
# Create your models here.

class Person(models.Model):
    age = models.IntegerField()
    birthday = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    freelance = models.CharField(max_length=5, default = True, choices = [['True', 'True'], ['False', 'False']])
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    details = models.TextField()
    description = models.CharField(max_length=355)
    image = models.ImageField(upload_to = 'images/')
    skills_description = models.TextField(null = True)
    
class Skill(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()
    def __str__(self):
        return self.name
    
class Project(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=500)
    completion_date = models.DateField()
    details = models.TextField(max_length=5000, null=True)
    image = models.ImageField(upload_to=project_image_path)
    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    image = models.ImageField(upload_to=project_images_path)
    
    def __str__(self):
        return f"Image of {self.project.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    read = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

