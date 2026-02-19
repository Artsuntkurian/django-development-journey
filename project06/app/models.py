from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    topic_no=models.IntegerField(null=True)
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    url=models.URLField()
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE,null=True)
    author=models.CharField(null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)