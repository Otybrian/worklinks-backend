# Generated by Django 3.2.10 on 2022-04-30 05:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='company_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobtype',
            field=models.TextField(choices=[('Part Time', 'Part-Time'), ('Remote', 'Remote'), ('Full Time', 'Full-Time')], max_length=30),
        ),
    ]