# Generated by Django 2.2.6 on 2019-11-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_auto_20191110_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.FileField(default='', upload_to='post_videos'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='', upload_to='post_images'),
        ),
    ]
