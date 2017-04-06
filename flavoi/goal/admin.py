from django.contrib import admin

from goal.models import Goal, GoalTheme

class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme', 'published', 'hot']

class GoalThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'color']

admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalTheme, GoalThemeAdmin)
