# Generated by Django 3.1 on 2020-08-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0002_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.BigIntegerField(unique=True),
        ),
    ]
