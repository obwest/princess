from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    search_fields = ('username', "email")
    list_display = ("fullname","username","email", 'is_active','is_admin', 'is_superuser')
    readonly_fields = ('last_login', 'date_created')

    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()
admin.site.register(Account, AccountAdmin)
