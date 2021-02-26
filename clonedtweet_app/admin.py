from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clonedtweet_app.models import CustomUser
# Register your models here.

OTHER_Field = (
    (None, {'fields': ('display_name',)}),
)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + OTHER_Field
    fieldsets = UserAdmin.fieldsets + OTHER_Field