# Generated by Django 3.0 on 2020-04-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thinkapp', '0005_auto_20200327_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='is_title',
            field=models.IntegerField(default='0', verbose_name='0，内容；1，标题'),
        ),
    ]
