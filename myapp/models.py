from django.db import models

class Question(models.model):
    question = models.CharField(max_length = 200)
    date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.FoeignKey(Question)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
