from django.db import models

# Create your models here.
class Project(models.Model): # This class is like a table in a database
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # This is a foreign key, which is a reference to another table