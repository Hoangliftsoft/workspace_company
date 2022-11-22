from django.db import models

# Create your models here.

class Question(models.Model):
    question_text= models.CharField(max_length=200)
    question_time= models.DateField()

class Choice(models.Model):
    choice_question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    choice_vote = models.IntegerField(default = 0)