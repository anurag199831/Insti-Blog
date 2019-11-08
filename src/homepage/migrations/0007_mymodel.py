# Generated by Django 2.2.6 on 2019-11-08 03:08

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20191106_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], max_length=49)),
            ],
        ),
    ]
