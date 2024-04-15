from django.contrib import admin
from CommentHandler.models import Comment

# Register your models here.
admin.site.site_header = 'CommentHandler'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentator', 'content', 'time', 'bugId')

admin.site.register(Comment,CommentAdmin)