# Generated by Django 4.2.13 on 2024-06-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, max_length=255),
        ),
    ]
