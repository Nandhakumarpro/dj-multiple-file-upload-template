from django.db import models

# Create your models here.


class Project(models.Model):
	project_name = models.CharField(max_length=20)
	project_summary = models.CharField(max_length=100)

class ProjectRefImages(models.Model):
	project = models.ForeignKey(Project, related_name=\
		'project_images', on_delete=models.CASCADE)
	image = models.ImageField(upload_to="uploads/")




