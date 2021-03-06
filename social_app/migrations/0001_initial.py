# Generated by Django 3.1 on 2020-08-21 02:35

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('activitytracking_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social_app.activitytracking')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile', models.BigIntegerField()),
                ('password', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='Profile_image/%Y/%m/%d')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='Profile_image/%Y/%m/%d')),
                ('address', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('relationship', models.BooleanField(default=False)),
                ('is_friend', models.BooleanField(default=False)),
                ('is_mutual', models.BooleanField(default=False)),
                ('is_married', models.BooleanField(default=False)),
            ],
            bases=('social_app.activitytracking',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('activitytracking_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social_app.activitytracking')),
                ('title', ckeditor.fields.RichTextField()),
                ('posts', ckeditor_uploader.fields.RichTextUploadingField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_app.users')),
            ],
            bases=('social_app.activitytracking',),
        ),
    ]
