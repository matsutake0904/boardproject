# Generated by Django 3.0.6 on 2020-12-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
