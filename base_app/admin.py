from django.contrib import admin
from base_app import models


# Register your models here.

@admin.site.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'points', 'is_staff', 'last_login']
    ordering = ['username', 'last_login']
    list_filter = ("is_staff",)
    fields = ("username", "email", "points")
    search_fields = ("username__startswith", "email__startswith")


admin.site.register(models.Rescue)
admin.site.register(models.Rescuer)
admin.site.register(models.RescueBoat)
admin.site.register(models.RescuedBoat)
admin.site.register(models.MedalOfHonor)
admin.site.register(models.RescueStation)
admin.site.register(models.Art)
admin.site.register(models.Quote)
