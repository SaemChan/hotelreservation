from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(
    models.User
)  # decorator  == admin.site.refgister(models.User, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "tophost",
                    "login_method",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("tophost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "tophost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
