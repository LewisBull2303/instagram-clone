# Generated by Django 4.2 on 2025-02-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(default='../Default_pfp_nxyoza.jpg', upload_to='images/'),
        ),
    ]
