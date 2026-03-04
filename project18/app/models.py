from django.db import models

# Create your models here.


class Topics(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=20)


class Webpage(models.Model):
    pass