from django.contrib import admin
from .models import User, Company, Tecnico, Scheme, Pedido


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
    list_display = ("id", "type_request", "scheme__name")
    list_filter = ["type_request", "scheme__name"]

admin.site.register(User, UserAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
admin.site.register(Scheme, SchemeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Pedido, PedidoAdmin)