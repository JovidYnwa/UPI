from django.contrib import admin
from .models import (UpiUser, 
                     UserAccount
                     )

class UpiUserAdmin(admin.ModelAdmin):
    #fields = ['phone', 'is_staff']
    list_display = ('phone', 'is_staff')


admin.site.register(UpiUser, UpiUserAdmin)
admin.site.register(UserAccount)

