# Generated by Django 4.2.13 on 2024-06-21 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_date_shipped_order_date_delivered_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='phone',
        ),
    ]
