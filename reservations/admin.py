from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservatiomnAdmin(admin.ModelAdmin):

    """ Revservation Admin Definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
