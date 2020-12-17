# Generated by Django 3.0.6 on 2020-12-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('auther', models.CharField(max_length=100, null=True)),
                ('images', models.ImageField(blank=True, upload_to='')),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('readtext', models.CharField(blank=True, default=' ', max_length=200, null=True)),
                ('branch', models.IntegerField(default=0)),
            ],
        ),
    ]
