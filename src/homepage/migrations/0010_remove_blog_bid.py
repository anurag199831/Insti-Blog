# Generated by Django 2.2.6 on 2019-11-09 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_blog_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='bid',
        ),
    ]