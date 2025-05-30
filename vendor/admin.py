from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Vendor,OpeningHour

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user','vendor_name','is_approved','created_at','modified_at')
    list_display_links = ('user','vendor_name')

class OpeningHourAdmin(admin.ModelAdmin):
    list_display=('vendor','day','from_hour','to_hour')


admin.site.register(Vendor,VendorAdmin)
admin.site.register(OpeningHour,OpeningHourAdmin)