from django.contrib import admin
from DataHandler.models import BugTuple

# Register your models here.
admin.site.site_header = 'BugHandler'
class BugTupleAdmin(admin.ModelAdmin):
    list_display = ('id','alias','summary','status','product','component','version','hardware','importance','QA','keywords','reported','modified','ccList','assignee')

admin.site.register(BugTuple, BugTupleAdmin)