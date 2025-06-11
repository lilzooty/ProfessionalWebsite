from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(null = True)
    #Should be nullable, some projects might not have an executable for the foreseeable future
    exeDownload = models.FileField(null=True)
    githubLink = models.URLField()
    description = models.TextField()


