from django.db import models
from django.db.models.fields import CharField, DateField, TextField
import datetime

class Day(models.Model):
    date = DateField(auto_now=False, auto_now_add=False, null=False, default=None)
    name = CharField(max_length=250, null=False, default=None)
    day_history = TextField(null=True)
    day_about = TextField(null=True)
    

