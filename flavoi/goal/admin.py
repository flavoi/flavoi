from django.contrib import admin

from goal.models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'percentage', 'published']

admin.site.register(Goal, GoalAdmin)
