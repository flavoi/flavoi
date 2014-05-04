from django.contrib import admin
from bio.models import Bio, Contact, Inspiration

class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"icon": ("label",)}

# Register your models here.
admin.site.register(Bio)
admin.site.register(Inspiration)
admin.site.register(Contact, ContactAdmin)