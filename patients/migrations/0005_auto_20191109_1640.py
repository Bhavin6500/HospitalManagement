# Generated by Django 2.2.6 on 2019-11-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20191109_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='medical_description',
            new_name='medical_history',
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='Hello', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='mrd_number',
            field=models.CharField(default='2019/09/11/121', max_length=20),
            preserve_default=False,
        ),
    ]