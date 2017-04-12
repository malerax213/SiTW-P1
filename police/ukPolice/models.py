from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Crime(models.Model):
    category = models.TextField(max_length=20)
    persisten_id = models.TextField(max_length=20, blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=date.today)
    policeman_assignated = models.ForeignKey(User, default='')


    #def get_absolute_url(self):
        #return reverse('ukPolice:Crime_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.category+"."+self.persisten_id


class Outcome(models.Model):
    code = models.TextField(max_length=30)
    name = models.TextField(max_length=30)
    Associated_crime = models.ForeignKey(Crime)

    def __unicode__(self):
        return self.Associated_crime.persisten_id+"."+self.name

class StreetLevelCrime(models.Model):
    crime = models.ForeignKey(Crime)
    street_id = models.TextField(max_length=20)
    street_name = models.TextField(max_length=20)
