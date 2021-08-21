from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
import datetime

class Day(models.Model):
    month = CharField(max_length=10, default=0)
    day = IntegerField(default=0)
    year = IntegerField(default = 0)
    name = CharField(max_length=250, null=False)
    day_history = TextField(null=True)
    day_about = TextField(null=True)
    

