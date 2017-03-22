from django.db import models

class Question(models.Model):
    question = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.choice
