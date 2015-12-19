# The main relationships reside here.

from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` field.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bio(TimeStampedModel):
    """
    A model that report the author life, hobbies and 
    contacts.
    """
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT+'profile_pic/', blank=True)
    cv = models.FileField(upload_to=settings.MEDIA_ROOT+'curriculum_vitae', blank=True)
    job_content = models.TextField()
    hobby_content = models.TextField()
    email = models.EmailField()
    active = models.BooleanField(default=True) 
    
    def __unicode__(self):
        return u'%s' % (self.title)


class Feature(models.Model):
    """
    This abstract class connect all the infos to the main 
    profile.
    """
    bio = models.ForeignKey(Bio)
    
    class Meta:
        abstract = True


class Contact(Feature):
    """
    A model that contains a bunch of helpful links.
    If primary it will be displayed in the first section of the webpage.
    """
    description = models.TextField(max_length=255, blank=True)
    label = models.CharField(max_length=30)
    link = models.URLField()
    icon = models.SlugField(max_length=30)
    primary = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.label)
    
    def save(self, *args, **kwargs):
      if not self.icon:
          self.icon = slugify(self.label)
      super(Contact, self).save(*args, **kwargs)


class Inspiration(Feature):
    """
    A collection of the best phrases I've ever heard.
    """
    quote = models.TextField(max_length=255)
    author = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % (self.author)