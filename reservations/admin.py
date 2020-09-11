from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservatiomnAdmin(admin.ModelAdmin):

    """ Revservation Admin Definition"""

    pass
