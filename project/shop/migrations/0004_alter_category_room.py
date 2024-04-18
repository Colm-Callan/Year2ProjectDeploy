# Generated by Django 5.0.2 on 2024-02-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='room',
            field=models.CharField(choices=[('bedroom', 'Bedroom'), ('kitchen', 'Kitchen'), ('living_room', 'Living Room'), ('bathroom', 'Bathroom'), ('dining_room', 'Dining Room')], default=None, max_length=200),
        ),
    ]