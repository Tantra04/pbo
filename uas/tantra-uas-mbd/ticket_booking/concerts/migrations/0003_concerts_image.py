# Generated by Django 5.1.5 on 2025-02-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0002_booking_confirmation_code_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='concerts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='concert_images/'),
        ),
    ]
