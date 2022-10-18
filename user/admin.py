from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from user.models import User, InvitedUser


# Register your models here.

class UserAdmin(ImportExportModelAdmin):
    exclude = ['user_type', ]


class InvitedUserAdmin(ImportExportModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(InvitedUser, InvitedUserAdmin)
