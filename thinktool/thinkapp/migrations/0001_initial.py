# Generated by Django 3.0 on 2020-03-23 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='框架')),
                ('F_id', models.IntegerField(default='0', verbose_name='frameid')),
                ('is_title', models.IntegerField(default='0', verbose_name='是否标题')),
                ('range_flage', models.IntegerField(default='0', verbose_name='属于第几个方案')),
                ('creater', models.CharField(max_length=64, verbose_name='创建人')),
                ('is_show', models.IntegerField(default=1, verbose_name='删除字段')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Sort_Detail',
            fields=[
                ('id', models.IntegerField(default='0', primary_key='True', serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='框架分类名称')),
                ('is_show', models.IntegerField(default=1, verbose_name='删除字段')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Frame_title',
            fields=[
                ('id', models.IntegerField(default='0', primary_key='True', serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='框架分类名称')),
                ('label', models.CharField(max_length=200, verbose_name='标签')),
                ('hide_input', models.IntegerField(default='1', verbose_name='0，子标题没有输入；1，有输入')),
                ('level', models.IntegerField(default='0', verbose_name='是否子标题')),
                ('creater', models.CharField(max_length=64, verbose_name='创建人')),
                ('is_show', models.IntegerField(default=1, verbose_name='删除字段')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('Sort_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thinkapp.Sort_Detail', verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Frame_content',
            fields=[
                ('id', models.IntegerField(default='0', primary_key='True', serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='框架分类名称')),
                ('creater', models.CharField(max_length=64, verbose_name='创建人')),
                ('is_show', models.IntegerField(default=1, verbose_name='删除字段')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('Frame_title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thinkapp.Frame_title', verbose_name='标题')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]