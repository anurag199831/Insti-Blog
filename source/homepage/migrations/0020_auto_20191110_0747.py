# Generated by Django 2.2.6 on 2019-11-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_auto_20191110_0653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='fileflag',
            new_name='imgflag',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='file',
            new_name='vid',
        ),
        migrations.AddField(
            model_name='blog',
            name='vidflag',
            field=models.BooleanField(default=False),
        ),
    ]