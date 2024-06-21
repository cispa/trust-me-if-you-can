from django.db import models


class Participation(models.Model):
    user = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    survey = models.JSONField()
