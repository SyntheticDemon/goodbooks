# Generated by Django 3.2.6 on 2021-09-22 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('digiapp', '0010_auto_20210922_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='written_time',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]