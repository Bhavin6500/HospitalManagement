# Generated by Django 2.2.6 on 2019-11-17 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_department_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='max_token',
            field=models.IntegerField(default=100),
        ),
    ]
