# Generated by Django 5.0.3 on 2024-06-04 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_order_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='order_placed_id',
        ),
    ]
