from django.contrib import admin

from provider.models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "api_key")
    search_fields = ("name",)
