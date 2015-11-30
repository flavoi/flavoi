"""
    Custom context processors for the page app.
    This script contains useful informations for every template.
"""
from django.conf import settings
from datetime import date

from .models import Bio, Inspiration


# Automatic copyright to the current year.
def copyright(request):
    START_YEAR = 2012
    this_year = date.today().year
    if START_YEAR != this_year:
        copy_year = "%s - %s" % (START_YEAR, this_year)
    else:
        copy_year = START_YEAR
    return { 'copyright': copy_year }

# The current Bio object is critical in many templates.
def profile(request):
    profile = Bio.objects.get(active=True)
    return { 'profile': profile }