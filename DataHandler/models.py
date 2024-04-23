from django.db import models

# Create your models here.
class  BugTuple(models.Model):
    id = models.IntegerField("id",primary_key=True) # bug id
    product = models.CharField("product",max_length=50) # bug所属的产品
    component = models.CharField("component",max_length=50) # bug所属的组件
    assignee = models.CharField("assignee",max_length=50) # bug负责人
    status = models.CharField("status",max_length=30) # bug状态限定值： IN P/ ACCE / NEW等
    summary = models.CharField("summary",max_length=300) # bug摘要
    version = models.CharField("version",max_length=30) # bug所属的版本
    platform = models.CharField("platform",max_length=50) # bug所属的平台
    op_sys = models.CharField("op_sys",max_length=50) # bug的操作系统
    priority = models.CharField("priority",max_length=30) # bug优先级： CRITICAL/MEDIUM/MEDIUM+/LOW/UNDECIDED"
    severity = models.CharField("severity",max_length=30) # bug严重程度限定值： CRITICAL/MAJOR/NORMAL/MINOR/ENHANCEMENT"
    QA = models.CharField("QA",max_length=50) # bug所属的QA(质量保证负责人)
    ccList = models.CharField("ccList",max_length=600) # bug抄送人员(一个列表)
    reportedId = models.IntegerField("id") # bug报告时间 (外键reportId)
    # modified # bug修改时间 (外键modifiedId列表)
    # comments # 评论

    class Meta:
        db_table = 'bug_tuple'
        verbose_name = 'BugTuple'
        verbose_name_plural = 'BugTuples'
        ordering = ['-reportedId']
        permissions = (
            ('my_view_bugtuple', '查看BugTuple'),
            ('my_add_bugtuple', '添加BugTuple'),)
        get_latest_by = 'reported'
        

    def __str__(self):
        return self.id

