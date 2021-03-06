# Generated by Django 3.2.6 on 2021-09-20 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digiapp', '0002_auto_20210918_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='good',
            name='tags',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='book', to='digiapp.good'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='subcategory',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subcatagory', to='digiapp.subcat'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='shopping_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_list', to='digiapp.good'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shopping_cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='digiapp.shoppingcart'),
        ),
    ]
