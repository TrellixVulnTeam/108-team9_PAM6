# Generated by Django 2.0 on 2019-06-03 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_list', '0002_auto_20190603_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store_list',
            old_name='main_image',
            new_name='image',
        ),
    ]
