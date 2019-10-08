from django.contrib import admin

from praca_inzynierska.models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Announcement, AnnouncementAdmin)
