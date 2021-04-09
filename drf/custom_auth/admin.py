from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Personal info', {'fields': ('id', 'username', 'balance')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )
    readonly_fields = ('id',)
