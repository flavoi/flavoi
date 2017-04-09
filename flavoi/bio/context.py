"""
    Custom context processors for the page app.
    This script contains useful informations for every template.
"""
from datetime import date

from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Bio, Contact


def signature(request):
    """ Automatic signature: FM YYYY-YYYY | social buttons """
    START_YEAR = 2016
    this_year = date.today().year
    if START_YEAR != this_year:
        copy_year = "%s - %s" % (START_YEAR, this_year)
    else:
        copy_year = START_YEAR
    signature = {
        'copy': "FM %s" % copy_year,
        'contacts': Contact.objects.filter(bio__active=True).order_by('-primary')
    }
    return signature 


def profile(request):
    """ An active Bio must always be present """
    profile = get_object_or_404(Bio, active=True)
    return { 'profile': profile }