from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_published = models.BooleanField(default=False)
