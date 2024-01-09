from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, OtpCode


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_staff', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('Main', {'fields': ('email', 'phone_number', 'first_name', 'last_name', 'password')}),
        ('Permissions',
         {'fields': ('is_staff', 'is_admin', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'first_name', 'last_name', 'password')}),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name',)


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
