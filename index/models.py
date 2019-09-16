from django.db import models
import datetime

# Create your models here.
class login(models.Model):
    u_phone = models.CharField(max_length=20, verbose_name='手机号')
    u_pass = models.CharField(max_length=50, verbose_name='密码')
    u_name = models.CharField(max_length=20, verbose_name='姓名')
    u_ID = models.CharField(max_length=18, verbose_name='身份证号')
    u_company = models.CharField(max_length=2, verbose_name='公司代码', null=True)
    u_department1 = models.CharField(max_length=2, verbose_name='一级部门代码', null=True)
    u_department2 = models.CharField(max_length=2, verbose_name='二级部门代码', null=True)
    u_post = models.CharField(max_length=10, verbose_name='岗位代码', null=True)
    is_Active = models.BooleanField(default=True, verbose_name='激活状态')
    picture = models.ImageField(null=True, upload_to = 'static/upload/usring', verbose_name='用户头像', default='/')
    level = models.IntegerField(verbose_name='用户权限', default=0)

    def __str__(self):
        return self.u_name

    class Meta:
        verbose_name = '人员管理'
        verbose_name_plural = verbose_name
        db_table = 'management'

