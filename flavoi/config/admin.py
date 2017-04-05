from django.contrib import admin
from django import forms
from django.db import models
from django.conf import settings

class RichModelAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    class Media:
        js = (settings.STATIC_URL + 'ckeditor/ckeditor.js',)
    class Meta:
        abstract = True
