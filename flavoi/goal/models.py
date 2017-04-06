
from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from fontawesome.fields import IconField

from bio.models import TimeStampedFeature


class GoalManager(models.QuerySet):
    
    # Get all the published goals from the active Bio 
    def get_all_active_goals(self):
        goals = self.filter(published=True).filter(bio__active=True)
        return goals

    # Get the list of published goals from the most recent to the least 
    def history(self):
        goals = self.get_all_active_goals().order_by('-hot', '-publication_date')
        return goals

    # Get the list of published goals in a set theme
    def get_goals_by_theme(self, theme_title):
        goals = self.history().filter(theme__title=theme_title)
        return goals

    # Get the hottest goal
    def get_hottest_goal(self):
        goal = self.history().filter(hot=True).latest('publication_date')
        return goal

    # Get the most recent goal
    def current(self):
        try:
            goal = self.get_hottest_goal()
        except ObjectDoesNotExist:
            goal = self.get_all_active_goals().latest('publication_date')
        return goal


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
    hot = models.BooleanField(default=False)
    theme = models.ForeignKey(GoalTheme, null=True, on_delete=models.SET_NULL)
    publication_date = models.DateField(auto_now_add=True)

    objects = GoalManager.as_manager()

    def __unicode__(self):
        return u'%s' % self.title

    # The following only changes pubblication date if published has been modified from False to True
    def __init__(self, *args, **kwargs):
        super(Goal, self).__init__(*args, **kwargs)
        self.old_published = self.published

    def save(self, *args, **kwargs):
        if self.old_published != self.published and self.published:
            self.publication_date = timezone.now()
        super(Goal, self).save(*args, **kwargs)