from django.contrib import admin

from .models import Goal, Theme, Attachment


class AttachmentInline(admin.TabularInline):
    model = Attachment
    fields = ('label', 'file')


class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme', 'published', 'hot']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        AttachmentInline,
    ]


admin.site.register(Goal, GoalAdmin)
admin.site.register(Theme)