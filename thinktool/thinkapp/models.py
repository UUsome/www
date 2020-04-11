from django.db import models


# Create your models here.
# 分类 TypeDetail (id,P_type,name,add_time,is_show,remark)
class Sort_Detail(models.Model):
    name = models.CharField(max_length=64,verbose_name='框架分类名称')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')

    # 定义表的属性信息
    class Meta:
        ordering = ["id"]

    # 定义静态方法
    def  __str__(self):
        return self.id,self.name, self.label, self.is_show


# 2，框架表设计 frame (id,type_id,order_flage,name,creater,add_time,is_show,remark)
class Frame_title(models.Model):
    name = models.CharField(max_length=64,verbose_name='框架分类名称')
    label = models.CharField(max_length=200,verbose_name='标签')
    Sort = models.ForeignKey(Sort_Detail, on_delete=models.CASCADE, null=False, verbose_name='类型')
    hide_input = models.IntegerField(default='1',verbose_name='0，子标题没有输入；1，有输入')
    level = models.IntegerField(default='0',verbose_name='是否子标题')
    # creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')

    # 定义静态方法
    def  __str__(self):
        return self.name


class Frame_content(models.Model):
    name = models.CharField(max_length=64,verbose_name='框架分类名称')
    Frame_title = models.ForeignKey(Frame_title, on_delete=models.CASCADE, null=False, verbose_name='标题')
    sub_title = models.IntegerField(default='1', verbose_name='0，子标题没有输入；1，有输入')
    # creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')

    # 定义表的属性信息
    class Meta:
        ordering = ["id"]

    # 定义静态方法
    def  __str__(self):
        return self.name


# 3，方案表设计 solution (s_order[第几个方案],frame_id,name,creater,add_time,is_show,remark)
class Solution(models.Model):
    F_id =  models.IntegerField(default='0',verbose_name='frameid')
    name = models.CharField(max_length=64,verbose_name='框架')
    is_title = models.IntegerField(default='0', verbose_name='0，内容；1，标题')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')
    # 定义静态方法
    def  __str__(self):
        return self.name

