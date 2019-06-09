# Generated by Django 2.0 on 2019-06-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store_list',
            old_name='image',
            new_name='main_image',
        ),
        migrations.AddField(
            model_name='store_list',
            name='hash_tag',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='store_list',
            name='sub_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='store_list',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='store_list',
            name='text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
