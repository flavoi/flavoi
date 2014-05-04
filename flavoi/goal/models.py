from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet

from bio.models import TimeStampedModel


class GoalManager(models.Manager):
    
    def get_query_set(self):
        return self.model.QuerySet(self.model)
    

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
    
    objects = GoalManager()

    class QuerySet(QuerySet):
        def current(self):
            return self.filter(
                published=True, 
                percentage__lt=100,
             ).latest('modified')

    def __unicode__(self):
        return u'%s' % self.title