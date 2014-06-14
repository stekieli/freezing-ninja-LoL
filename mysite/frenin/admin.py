from django.contrib import admin
from frenin.models import UserProfile
# Register your models here.

#class UPAdmin(admin.ModelAdmin):
#    fields = ['username', 'password']

admin.site.register(UserProfile)#,UPAdmin)
