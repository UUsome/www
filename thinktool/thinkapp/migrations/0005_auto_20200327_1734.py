# Generated by Django 3.0 on 2020-03-27 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thinkapp', '0004_frame_content_sub_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='is_title',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='range_flage',
        ),
    ]
