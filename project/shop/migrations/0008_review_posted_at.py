# Generated by Django 4.2.5 on 2024-03-18 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
