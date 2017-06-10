# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Destination(models.Model):
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=50)
    duration = models.IntegerField('days')
    from_date = models.DateTimeField('Arrive')
    to_date = models.DateTimeField('Depart')
