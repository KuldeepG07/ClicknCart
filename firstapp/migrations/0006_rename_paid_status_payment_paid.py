# Generated by Django 5.0.3 on 2024-05-28 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_rename_pay_order_id_payment_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paid_status',
            new_name='paid',
        ),
    ]