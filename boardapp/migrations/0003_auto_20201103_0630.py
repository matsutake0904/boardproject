# Generated by Django 3.0.6 on 2020-11-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_auto_20200517_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='branch',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]