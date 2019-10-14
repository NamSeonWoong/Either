from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=150)
    question1 = models.CharField(max_length=150)
    question2= models.CharField(max_length=150)

class Choice(models.Model):
    content = models.CharField(max_length=200)
    pick = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
