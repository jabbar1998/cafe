# Generated by Django 5.0.1 on 2024-01-05 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_user_order_costumer_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='costumer_phone_number',
            new_name='customer_phone_number',
        ),
    ]
