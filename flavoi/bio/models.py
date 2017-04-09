# The main relationships reside here.

from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from ckeditor.fields import RichTextField


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
    picture = models.ImageField(upload_to='media/bio/', blank=True)
    cv = models.FileField(upload_to='media/bio/', blank=True)
    job_content = RichTextField()
    hobby_content = RichTextField()
    email = models.EmailField()
    active = models.BooleanField(default=True) 
    
    def __unicode__(self):
        return u'%s' % (self.title)


class Feature(models.Model):
    """
    This abstract class connect all the infos to the main 
    profile.
    """
    bio = models.ForeignKey(
        Bio,
        null=True,
        on_delete=models.SET_NULL,
        primary_key=False,
    )
    
    class Meta:
        abstract = True


class TimeStampedFeature(TimeStampedModel):
    """
    This class is suited for features with a creation date.
    """
    bio = models.ForeignKey(
        Bio,
        null=True,
        on_delete=models.SET_NULL,
        primary_key=False,
    )
    
    class Meta:
        abstract = True


class Contact(Feature):
    """
    The list of links that can be used to keep in touch.
    If primary it will be highlighted.
    """
    description = models.TextField(max_length=255, blank=True)
    label = models.CharField(max_length=30)
    link = models.URLField()
    icon = models.CharField(max_length=40)
    primary = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.label)


class Inspiration(Feature):
    """
    A collection of the best phrases I've ever heard.
    """
    quote = models.TextField(max_length=255)
    author = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % (self.author)


class Momenti(Feature):
    """
        A collection of the best moments of my life.
    """
    photo = models.ImageField(upload_to='media/momenti/')
    caption = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.caption)

    class Meta:
        verbose_name_plural = "momenti"