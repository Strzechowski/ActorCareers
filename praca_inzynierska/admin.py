from django.contrib import admin

from praca_inzynierska.models import Announcement, Actor, Category

class AnnouncementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Announcement, AnnouncementAdmin)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')
    orderding = ('surname')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )