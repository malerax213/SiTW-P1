from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from forms import SignUpForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ukPolice.models import Outcome, NeighbourhoodPriority

@login_required()
def home(request):
    return render_to_response('home.html', {
        'user': request.user
    })

def main(request):
    return render_to_response('main.html')

def signup(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('signup.html', data)

def crimes(request):
    user = User.objects.get(username=request.user)
    crimes = user.crime_set.all()

    return render_to_response('crimes.html', {
        'username': request.user,
        'crimes': crimes
    })

def outcomes(request):
    outcomes = Outcome.objects.all()

    return render_to_response('outcomes.html', {
        'outcomes': outcomes
    })

def neighbourhoodpriorities(request):
    np = NeighbourhoodPriority.objects.all()

    return render_to_response('neighbourhoodpriorities.html', {
        'np': np 
    })
