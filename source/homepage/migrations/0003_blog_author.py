# Generated by Django 2.2.6 on 2019-11-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20191028_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]