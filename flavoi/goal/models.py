from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet
from django.conf import settings

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from fontawesome.fields import IconField

from bio.models import TimeStampedFeature


class GoalManager(models.QuerySet):
    
    # Get all the published goals from the active Bio 
    def get_all_active_goals(self):
        goals = self.filter(published=True).filter(bio__active=True)
        return goals

    # Get the most recent goal
    def current(self):
        current_goal = self.get_all_active_goals().latest('modified')
        return current_goal

    # Get the list of published goals from the most recent to the least 
    def history(self):
        goals = self.get_all_active_goals().order_by('-modified')
        return goals

    # Get the list of published goals in the set year
    def get_year_archive(self, year):
        goals = self.get_all_active_goals().filter(created__year=year)
        return goals

    # Get the list of published goals in the set month
    def get_month_archive(self, year, month):
        goals = self.get_year_archive(year).filter(created__month=month)
        return goals

    # Get the list of published goals in a set theme
    def get_goals_by_theme(self, theme_title):
        goals = self.get_all_active_goals().filter(theme__title=theme_title)
        return goals


class GoalTheme(TimeStampedFeature):
    """
        Defines the theme and the argument of a certain goal.
    """
    title = models.CharField(max_length=60, unique=True)
    icon = IconField()
    color = ColorField()

    def __unicode__(self):
        return u'%s' % (self.title)


class Goal(TimeStampedFeature):
    """
        Personal and current projects or achievements.
        To add: work in progress details.
    """
    title = models.CharField(max_length=60)
    abstract = RichTextField()
    description = RichTextField()
    published = models.BooleanField(default=False)
    percentage = PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
        ]
     )
    theme = models.ForeignKey(GoalTheme, null=True, on_delete=models.SET_NULL)

    objects = GoalManager.as_manager()

    def __unicode__(self):
        return u'%s' % self.title