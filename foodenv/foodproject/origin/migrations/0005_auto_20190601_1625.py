# Generated by Django 2.0 on 2019-06-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('origin', '0004_auto_20190601_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origin',
            name='image',
            field=models.ImageField(height_field='height', null=True, upload_to='', width_field='width'),
        ),
    ]
