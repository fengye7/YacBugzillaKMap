from django.contrib import admin
from RecordsHandler.models import Reported,Modified

# Register your models here.
admin.site.site_header = 'RecordsHandler'
class ReportedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','time','bugId')

admin.site.register(Reported, ReportedAdmin)

class ModifiedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','time','bugId')

admin.site.register(Modified, ModifiedAdmin)