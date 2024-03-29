from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username
