# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from .forms import NameForm, ItineraryForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_name(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
        # create a form instance and populate it with data from the request:
    form = NameForm(request.POST)
        # check whether it's valid:
    if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

def get_itinerary(request):
    form = ItineraryForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/thanks/')
    else:
        form = ItineraryForm()
    return render(request, 'polls/itinerary.html', {'form': form})
# def home(request):
    # labels
    # city, state
    # days
    # from, to
