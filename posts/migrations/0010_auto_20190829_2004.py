# Generated by Django 2.2.4 on 2019-08-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190829_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/static/images/placeholder.png', upload_to='images'),
        ),
    ]
