from django.contrib import admin
from .models import User, Company, Tecnico, Scheme, Pedido

admin.site.register(User)
admin.site.register(Tecnico)
admin.site.register(Scheme)
admin.site.register(Company)
admin.site.register(Pedido)