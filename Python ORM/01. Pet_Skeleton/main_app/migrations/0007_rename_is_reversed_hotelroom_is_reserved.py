# Generated by Django 5.0.4 on 2024-05-16 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_hotelroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelroom',
            old_name='is_reversed',
            new_name='is_reserved',
        ),
    ]
