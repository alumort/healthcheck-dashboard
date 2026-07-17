from django.contrib import admin

from .models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("nombre","url","activo","created_at",)

    list_per_page = 15

    list_display_links = ("nombre",)

    search_fields = ("nombre","url",)

    list_filter = ("activo",)

    readonly_fields = ("created_at","updated_at",)
