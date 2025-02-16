from django.contrib import admin
from django.contrib.admin import ShowFacets
from django.contrib.auth.admin import UserAdmin

from user.models import UserModel


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    show_facets = ShowFacets.NEVER
    add_fieldsets = (
        (None, {
            "fields": ("username", "email", "password1", "password2"),
            "classes": ("wide",),
        }),
    )
