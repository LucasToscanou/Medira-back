from django.db import models

class WeightRecord(models.Model):
    weight = models.FloatField();
    date = models.DateTimeField();
