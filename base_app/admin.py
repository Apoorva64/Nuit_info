from django.contrib import admin
from base_app import models

# Register your models here.
print(models.Rescuer)


class RescuedBoatAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_plate', 'has_been_published']
    ordering = ['name']


class RescueBoatAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_plate', 'start_date', 'has_been_published']
    ordering = ['name']


class MedalOfHonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'has_been_published']


class RescuerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'has_been_published']


class RescueAdmin(admin.ModelAdmin):
    list_display = ['rescue_date', 'number_of_saved_people', 'has_been_published']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'points', 'is_staff', 'last_login']
    ordering = ['username', 'last_login']
    list_filter = ("is_staff",)
    exclude = ('password',)
    search_fields = ("username__startswith", "email__startswith")


class RescueStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'has_been_published']


class ArtAdmin(admin.ModelAdmin):
    list_display = ['author', 'type', 'creation_date', 'editor_name', 'name', 'description', 'has_been_published']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['content', 'rescue', 'rescuer', 'has_been_published']


admin.site.register(models.RescuedBoat, RescuedBoatAdmin)
admin.site.register(models.RescueBoat, RescueBoatAdmin)
admin.site.register(models.MedalOfHonor, MedalOfHonorAdmin)

admin.site.register(models.Rescue, RescueAdmin)
admin.site.register(models.Rescuer, RescuerAdmin)
admin.site.register(models.RescueStation, RescueStationAdmin)
admin.site.register(models.Art, ArtAdmin)
admin.site.register(models.Quote, QuoteAdmin)
admin.site.register(models.User, UserAdmin)
