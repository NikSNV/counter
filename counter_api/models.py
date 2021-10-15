from django.db import models


class Counter(models.Model):
    date = models.DateField()
    views = models.IntegerField()
    clicks = models.IntegerField()
    cost = models.FloatField()
    # cpc = models.FloatField(default=0)
    # cpm = models.FloatField(default=0)
