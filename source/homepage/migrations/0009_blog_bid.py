# Generated by Django 2.2.6 on 2019-11-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bid',
            field=models.CharField(default='', max_length=150),
        ),
    ]
