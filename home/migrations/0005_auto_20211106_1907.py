# Generated by Django 3.1.4 on 2021-11-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211106_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='like_post',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='like_post',
            field=models.IntegerField(blank=True, default=int),
            preserve_default=False,
        ),
    ]
