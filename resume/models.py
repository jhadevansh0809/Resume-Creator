from django.db import models

# Create your models here.

class Resume(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    skills=models.CharField(max_length=1000)
    university=models.CharField(max_length=300)
    university_score=models.CharField(max_length=10,default="")
    twelveth_schooling=models.CharField(max_length=300,default="")
    twelveth_score=models.CharField(max_length=10,default="")
    tenth_schooling=models.CharField(max_length=300,default="")
    tenth_score=models.CharField(max_length=10,default="")
    experience=models.TextField()
    projects=models.TextField()
    languages=models.CharField(max_length=1000)
    awards=models.TextField()