from django.db import models

# Create your models here.
# 留言板
class contact(models.Model):
    title = models.CharField(max_length=64,null=True,verbose_name='主题')
    contact = models.CharField(max_length=64,null=True, verbose_name='联系方式')
    content = models.CharField(max_length=200,null=True, verbose_name='联系方式')
    add_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
