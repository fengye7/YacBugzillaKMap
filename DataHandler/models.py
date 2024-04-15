from django.db import models

# Create your models here.
class  BugTuple(models.Model):
    id = models.IntegerField("id",primary_key=True) # bug id
    alias = models.CharField("alias", max_length=50) # bug别名，唯一标识
    summary = models.CharField("summary",max_length=300) # bug摘要
    status = models.CharField("status",max_length=10) # bug状态限定值： IN P/ ACCE / NEW等
    product = models.CharField("product",max_length=50) # bug所属的产品
    component = models.CharField("component",max_length=50) # bug所属的组件
    version = models.CharField("version",max_length=10) # bug所属的版本
    hardware = models.CharField("hardware",max_length=50) # bug所属的硬件
    importance = models.CharField("importance",max_length=10) # bug重要程度限定值： CRITICAL/HIGH/MEDIUM/LOW"
    QA = models.CharField("QA",max_length=50) # bug所属的QA(质量保证负责人)
    keywords = models.CharField("keywords",max_length=200) # bug关键字
    reported = models.DateTimeField("reported") # bug报告时间"
    modified = models.DateTimeField("modified") # bug修改时间
    ccList = models.CharField("ccList",max_length=200) # bug抄送人员
    assignee = models.CharField("assignee",max_length=50) # bug负责人

    class Meta:
        db_table = 'bug_tuple'
        verbose_name = 'BugTuple'
        verbose_name_plural = 'BugTuples'
        ordering = ['-reported']
        unique_together = (('alias','summary'),)
        indexes = [
            models.Index(fields=['alias','summary']),
        ]
        permissions = (
            ('my_view_bugtuple', '查看BugTuple'),
            ('my_add_bugtuple', '添加BugTuple'),)
        get_latest_by = 'reported'
        

    def __str__(self):
        return self.alias

