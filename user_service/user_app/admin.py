from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)

from .models import ProContentCreatorPermissions

class ProContentCreatorPermissionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProContentCreatorPermissions, ProContentCreatorPermissionsAdmin)