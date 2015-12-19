from django.contrib import admin

from flavoi.admin import RichModelAdmin
from bio.models import Bio, Contact, Inspiration

class BioAdmin(RichModelAdmin):
    list_display = ['title', 'subtitle', 'active']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['label', 'link', 'primary']
    prepopulated_fields = {"icon": ("label",)}

# Register your models here.
admin.site.register(Bio, BioAdmin)
admin.site.register(Inspiration)
admin.site.register(Contact, ContactAdmin)