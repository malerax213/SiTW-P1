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

    def __unicode__(self):
        return self.crime+"."+self.street_name

class StreetLevelOutcome(models.Model):
    outcome = models.ForeignKey(Outcome)
    street_id = models.TextField(max_length=20)
    street_name = models.TextField(max_length=20)

    def __unicode__(self):
        return self.outcome+"."+self.street_name

class Neighbourhood(models.Model):
    n_id = models.TextField(max_length=20)
    n_name = models.TextField(max_length=30)

    def __unicode__(self):
        return self.n_id+"."+self.n_name

class NeighbourhoodPriority(models.Model):
    action = models.TextField(max_length=20,blank=True,null=True)
    action_date = models.DateField(default=date.today,blank=True,null=True)
    issue = models.TextField(max_length=50)
    issue_date = models.DateField(default=date.today)
    neighbourhood = models.ForeignKey(Neighbourhood)

    def __unicode__(self):
        return str(self.neighbourhood)+"."+str(self.issue_date)
