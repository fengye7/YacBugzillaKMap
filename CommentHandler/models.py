from django.db import models
from DataHandler.models import BugTuple

# Create your models here.
class Comment(models.Model):
    id = models.IntegerField("id",primary_key=True) # Unique identifier for the comment
    commentator = models.CharField("commentator",max_length=50) # bug评论者
    content = models.TextField("content", max_length = 300) # bug评论内容
    time = models.DateTimeField("time") # bug评论时间
    bugId =  models.IntegerField("Bug ID") # 外键bug id

    class Meta:
        db_table = "comment"
        verbose_name = "bug评论"
        verbose_name_plural = "bug评论(s)"
        ordering = ["-time"]
        indexes = [
            models.Index(fields=["time"]),
        ]
        permissions = (
            ("can_view_comment", "Can view comment"),
        )
        managed = True
        get_latest_by = "time"

    def __str__(self):
        return self.id