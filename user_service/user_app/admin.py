from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)

from .models import  ContentCreatorProfile, RegularUserProfile ,RegularProUserPermission, ContentCreatorProUserPermission


admin.site.register(ContentCreatorProfile)
admin.site.register(RegularUserProfile)
admin.site.register(RegularProUserPermission)
admin.site.register(ContentCreatorProUserPermission)