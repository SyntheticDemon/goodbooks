# Generated by Django 3.2.6 on 2021-09-24 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digiapp', '0014_alter_review_reviewer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='descritpion',
            new_name='description',
        ),
    ]
