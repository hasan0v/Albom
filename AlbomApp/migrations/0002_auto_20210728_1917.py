# Generated by Django 3.2.5 on 2021-07-28 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlbomApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
