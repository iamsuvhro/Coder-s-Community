# Generated by Django 3.1.4 on 2021-11-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211106_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='_like_post',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='like_post',
            field=models.IntegerField(default=int),
            preserve_default=False,
        ),
    ]