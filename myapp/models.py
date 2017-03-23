from django.db import models
from django.utils import *
from datetime import datetime, timedelta

class Question(models.Model):
    question = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.date >=datetime.now(timezone.utc) + timedelta(days=-1)
    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.choice
