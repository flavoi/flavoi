from django.contrib import admin

from flavoi.admin import RichModelAdmin
from goal.models import Goal

class GoalAdmin(RichModelAdmin):
    list_display = ['title', 'percentage', 'published']

admin.site.register(Goal, GoalAdmin)
