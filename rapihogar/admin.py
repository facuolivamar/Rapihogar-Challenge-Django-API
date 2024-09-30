from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import User, Company, Tecnico, Scheme, Pedido


# Register your models here.
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"

    # to filter the resultes by users, content types and action flags
    list_filter = ["user", "content_type", "action_flag"]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = ["object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "content_type",
        "action_flag",
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email")
    list_filter = ["is_active", "is_staff"]


class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", )


class SchemeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "website")


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "type_request", "scheme__name", "technician")
    list_filter = ["type_request", "scheme__name"]


admin.site.register(User, UserAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
admin.site.register(Scheme, SchemeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Pedido, PedidoAdmin)
