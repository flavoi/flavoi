"""
    Custom context processors for the page app.
    This script contains useful informations for every template.
"""
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Bio


""" 
    An active Bio must always be present.
"""
def profile(request):
    profile = get_object_or_404(Bio, active=True)
    return { 'profile': profile }