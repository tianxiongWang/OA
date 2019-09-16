
from django.db import models

# Create your models here.


# 入职安全考试题数据库关系映射
class rzaqks(models.Model):
    # 单选框
    select_type = (('1', '单项选择题'), ('2', '多项选择题'), ('3', '判断题'), ('4', '简答'))
    question_type = models.CharField(max_length=2,
                                     verbose_name='题型',
                                     choices=select_type,
                                     )
    # 题目内容
    subject = models.CharField(max_length=300, verbose_name='题目')
    # 选项
    a_option = models.CharField(max_length=100, verbose_name='A选项', null=True)
    b_option = models.CharField(max_length=100, verbose_name='B选项', null=True)
    c_option = models.CharField(max_length=100, verbose_name='C选项', null=True)
    d_option = models.CharField(max_length=100, verbose_name='D选项', null=True)
    # 答案选项
    answer = models.CharField(max_length=10, verbose_name='答案')

    # 数据库表名
    class Meta:
        db_table = 'rzaqks'

# 入职安全考试成绩数据库关系映射
class rzaqks_score(models.Model):
    first = models.CharField(max_length=3, verbose_name='第一次成绩', null=True)
    second = models.CharField(max_length=3, verbose_name='第二次成绩', null=True)
    third = models.CharField(max_length=3, verbose_name='第三次成绩', null=True)
    class Meta:
        verbose_name = '入职安全考成绩'
        verbose_name_plural = verbose_name
        db_table = 'rzaqks_score'

# 入职测试数据库关系映射
class rzcsks(models.Model):
    # 单选框
    question_type = models.CharField(max_length=2, )
    # 题目内容
    subject = models.CharField(max_length=300, verbose_name='题目')
    # 选项
    a_option = models.CharField(max_length=300, verbose_name='A选项', null=True)
    b_option = models.CharField(max_length=300, verbose_name='B选项', null=True)
    c_option = models.CharField(max_length=300, verbose_name='C选项', null=True)
    d_option = models.CharField(max_length=300, verbose_name='D选项', null=True)
    # 答案选项
    answer = models.CharField(max_length=300, verbose_name='答案')
    # 数据库表名
    class Meta:
        db_table = 'rzcsks'
# 入职测试
class rzcsks_score(models.Model):
    login_id = models.CharField(max_length=10, verbose_name='login_id', null=True)
    first = models.CharField(max_length=3, verbose_name='第一次成绩', null=True)
    second = models.CharField(max_length=3, verbose_name='第二次成绩', null=True)
    third = models.CharField(max_length=3, verbose_name='第三次成绩', null=True)
    class Meta:
        db_table = 'rzcsks_score'
