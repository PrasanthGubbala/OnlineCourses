# Generated by Django 2.2.4 on 2020-07-17 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200712_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 17, 18, 3, 52, 677728)),
        ),
        migrations.AlterField(
            model_name='enrolledcourses',
            name='course_id',
            field=models.IntegerField(unique=True),
        ),
    ]
