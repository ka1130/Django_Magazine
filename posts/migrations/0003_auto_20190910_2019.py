# Generated by Django 2.2.5 on 2019-09-10 20:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190830_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]