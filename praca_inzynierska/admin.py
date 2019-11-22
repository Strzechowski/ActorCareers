from django.contrib import admin

from praca_inzynierska.models import Actor, Category, Company, Job


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')
    orderding = ('surname')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', )