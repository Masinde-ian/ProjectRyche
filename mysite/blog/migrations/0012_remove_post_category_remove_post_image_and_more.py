# Generated by Django 4.2.13 on 2024-06-28 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sub_title',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
