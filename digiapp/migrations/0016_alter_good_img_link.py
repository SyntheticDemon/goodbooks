# Generated by Django 3.2.6 on 2021-09-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiapp', '0015_rename_descritpion_good_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='img_link',
            field=models.CharField(max_length=2000),
        ),
    ]
