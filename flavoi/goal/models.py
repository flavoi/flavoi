from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import PositiveIntegerField

from bio.models import TimeStampedModel

    
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

    def __unicode__(self):
        return u'%s' % self.title