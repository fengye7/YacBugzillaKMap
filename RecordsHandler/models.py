from django.db import models
from DataHandler.models import BugTuple

# Create your models here.
class Reported(models.Model):
    id = models.IntegerField("id",primary_key=True)
    user = models.CharField("user", max_length=50) # bug报告者
    time = models.DateTimeField("time",auto_now_add=True) # bug报告时间
    bugId = models.ForeignKey(BugTuple,on_delete=models.PROTECT,related_name="bug_reported",to_field="id",verbose_name="Bug ID") # 外键bug id

    class Meta:
        db_table = "reported"
        verbose_name = "bug报告"
        verbose_name_plural = "bug报告(s)"
        ordering = ["-time"]
        indexes = [
            models.Index(fields=["time"]),
        ]
        permissions = (
            ("can_view_reported", "Can view reported"),
        )
        managed = True
        get_latest_by = "time"

    def __str__(self):
        return self.id
    

class Modified(models.Model):
    id = models.IntegerField("id",primary_key=True)
    user = models.CharField("user", max_length=50) # bug修改者
    time = models.DateTimeField("time",auto_now_add=True) # bug修改时间
    bugId = models.ForeignKey(BugTuple,on_delete=models.PROTECT,related_name="bug_modified",to_field="id",verbose_name="Bug ID") # 外键bug id

    class Meta:
        db_table = "modified"
        verbose_name = "bug修改"
        verbose_name_plural = "bug修改(s)"
        ordering = ["-time"]
        indexes = [
            models.Index(fields=["time"]),
        ]
        permissions = (
            ("can_view_modified", "Can view modified"),
        )
        managed = True
        get_latest_by = "time"

    def __str__(self):
        return self.id