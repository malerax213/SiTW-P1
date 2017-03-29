from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Crime(models.Model):
    category = models.TextField()
    persisten_id = models.TextField(blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    # user = models.ForeignKey(User, default=1) # Para usos posteriores
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('ukPolice:Crime_detail', kwargs={'pk': self.pk})
