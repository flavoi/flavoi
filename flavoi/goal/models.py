from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet
from django.conf import settings

from bio.models import TimeStampedModel, Bio


class GoalManager(models.QuerySet):
    
    # Get the most recent goal
    def current(self):
        current_goal = self.filter(published=True).filter(bio__active=True).latest('modified')
        return current_goal

    # Get the list of published goals from the most recent to the least 
    def history(self):
        goals = self.filter(published=True).filter(bio__active=True).order_by('-modified')
        return goals

    # Get the list of published goals in the set year
    def get_year_archive(self, year):
        goals = self.filter(published=True).filter(bio__active=True).filter(created__year=year)
        return goals

    # Get the list of published goals in the set month
    def get_month_archive(self, year, month):
        goals = self.get_year_archive(year).filter(bio__active=True).filter(created__month=month)
        return goals
        

class Goal(TimeStampedModel):
    """
        Personal and current projects or achievements.
        To add: work in progress details.
    """
    title = models.CharField(max_length=60)
    abstract = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    percentage = PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
        ]
     )
    bio = models.ForeignKey(
        Bio,
        null=True,
        on_delete=models.SET_NULL,
        primary_key=False,
    )
    
    objects = GoalManager.as_manager()

    def __unicode__(self):
        return u'%s' % self.title