from django.db import models
from django.db.models.fields import CharField, DateField

class Day(models.Model):
    date = DateField(auto_now=False, auto_now_add=False, null=False)
    name = CharField(max_length=250)
