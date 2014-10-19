from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet

from bio.models import TimeStampedModel


class GoalManager(models.QuerySet):
    
    # Get the latest goal, it will be shown at the homepage
    def current(self):
        return self.filter(published=True, percentage__lt=100).latest('modified')
    

class Goal(TimeStampedModel):
    """
        Personal and current projects or achievements.
        To add: work in progress details.
    """
    title = models.CharField(max_length=60)
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