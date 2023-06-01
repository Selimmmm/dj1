from django.contrib import admin

from .models import TimeSlot


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "slot_type",
        "date_start",
        "date_end",
        "date_created",
    )


admin.site.register(TimeSlot, TimeSlotAdmin)
