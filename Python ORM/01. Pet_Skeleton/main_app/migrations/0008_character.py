# Generated by Django 5.0.4 on 2024-05-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_is_reversed_hotelroom_is_reserved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.CharField(choices=[('Mage', 'Mage'), ('Warrior', 'Warrior'), ('Assassin', 'Assassin'), ('Scout', 'Scout')], max_length=20)),
                ('level', models.PositiveIntegerField()),
                ('strength', models.PositiveIntegerField()),
                ('dexterity', models.PositiveIntegerField()),
                ('intelligence', models.PositiveIntegerField()),
                ('hit_points', models.PositiveIntegerField()),
                ('inventory', models.TextField()),
            ],
        ),
    ]
