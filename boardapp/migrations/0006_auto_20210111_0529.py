# Generated by Django 3.0.6 on 2021-01-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0005_boardmodel_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
