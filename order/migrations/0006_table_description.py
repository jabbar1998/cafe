# Generated by Django 5.0.1 on 2024-01-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_rename_avalability_table_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
