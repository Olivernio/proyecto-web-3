from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)

# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)