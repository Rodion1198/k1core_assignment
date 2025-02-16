from django.contrib import admin

from block.models import Block, Currency


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("id", "currency", "provider", "number", "created_at", "stored_at")
    search_fields = ("currency__name", "number")
    list_filter = ("currency", "provider")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("currency", "provider")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
