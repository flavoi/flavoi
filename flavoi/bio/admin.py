from django.contrib import admin

from bio.models import Bio, Contact, Inspiration, Momenti

class BioAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'surname', 'active']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['label', 'link', 'primary']

# Register your models here.
admin.site.register(Bio, BioAdmin)
admin.site.register(Inspiration)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Momenti)