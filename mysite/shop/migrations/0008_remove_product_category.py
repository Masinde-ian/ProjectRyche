# Generated by Django 4.2.13 on 2024-07-02 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_image_alter_product_image2_review_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
