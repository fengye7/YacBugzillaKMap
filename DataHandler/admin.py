from django.contrib import admin
from DataHandler.models import BugTuple

# Register your models here.
admin.site.site_header = 'BugHandler'
class BugTupleAdmin(admin.ModelAdmin):
    list_display = ('id','product','component','assignee','status','summary','version','platform', 'op_sys','priority','severity','QA','ccList','reportedId')

admin.site.register(BugTuple, BugTupleAdmin)