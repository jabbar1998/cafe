# Generated by Django 5.0.1 on 2024-01-05 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_costumer_phone_number_order_customer_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='avalability',
            new_name='availability',
        ),
    ]