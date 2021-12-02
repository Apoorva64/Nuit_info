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
    list_display = ['first_name', 'last_name']


class RescueAdmin(admin.ModelAdmin):
    list_display = ['rescue_date', 'number_of_saved_people']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'points', 'is_staff', 'last_login']
    ordering = ['username', 'last_login']
    list_filter = ("is_staff",)
    exclude = ('password',)
    search_fields = ("username__startswith", "email__startswith")


admin.site.register(models.RescuedBoat, RescuedBoatAdmin)
admin.site.register(models.RescueBoat, RescueBoatAdmin)
admin.site.register(models.MedalOfHonor, MedalOfHonorAdmin)

admin.site.register(models.Rescue)
admin.site.register(models.Rescuer)
admin.site.register(models.RescueStation)
admin.site.register(models.Art)
admin.site.register(models.Quote)
admin.site.register(models.User, UserAdmin)
