# Generated by Django 2.2.6 on 2019-11-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='', upload_to='post_images'),
        ),
    ]