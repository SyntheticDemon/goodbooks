# Generated by Django 3.2.6 on 2021-09-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiapp', '0005_auto_20210920_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='author',
        ),
        migrations.AlterField(
            model_name='good',
            name='average_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='checkout_price',
            field=models.IntegerField(default=0),
        ),
    ]