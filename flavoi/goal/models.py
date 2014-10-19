from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet
from django.conf import settings

from bio.models import TimeStampedModel


class GoalManager(models.QuerySet):
    
    # Get the most recent goal giving priority to works in progress
    def current(self):
        current_goal = None
        try:
            current_goal = self.filter(published=True, percentage__lt=100).latest('modified')
        except:
            curret_goal = self.filter(published=True).latest('modified')
        return current_goal


class Goal(TimeStampedModel):
    """
        Personal and current projects or achievements.
        To add: work in progress details.
    """
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT+'goals/', blank=True, null=True)
    published = models.BooleanField(default=False)
    percentage = PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
        ]
     )
    
    objects = GoalManager.as_manager()

    def __unicode__(self):
        return u'%s' % self.title