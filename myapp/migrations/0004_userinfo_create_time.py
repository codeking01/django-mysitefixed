# Generated by Django 4.0.5 on 2022-06-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_userinfo_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='入职时间'),
        ),
    ]
