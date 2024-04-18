# Generated by Django 5.0.2 on 2024-02-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='room',
            field=models.CharField(choices=[('bedroom', 'Bedroom'), ('kitchen', 'Kitchen'), ('living_room', 'Living Room'), ('bathroom', 'Bathroom'), ('garden', 'Garden')], default=None, max_length=200),
        ),
    ]
