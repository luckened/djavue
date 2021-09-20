from django.contrib import admin

from core.models import ActivityLog, Tweet


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Tweet, TweetAdmin)
