# Generated by Django 3.2.6 on 2021-09-17 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_link', models.TextField(max_length=200)),
                ('title', models.TextField(max_length=200)),
                ('descritpion', models.TextField(max_length=200)),
                ('color', models.CharField(choices=[('GREEN', 'green'), ('BLUE', 'black'), ('YELLOW', 'yellow'), ('RED', 'Red'), ('WHITE', 'White'), ('BLACK', 'Black'), ('NOCOLOR', '')], default='NOCOLOR', max_length=9)),
                ('price', models.IntegerField()),
                ('average_rating', models.IntegerField()),
                ('category', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_price', models.IntegerField(default=0)),
                ('checked_out', models.BooleanField(default=False)),
                ('shopping_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digiapp.good')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dated_joined', models.DateTimeField(auto_created=True)),
                ('address', models.TextField(max_length=200)),
                ('zip_code', models.TextField(max_length=200)),
                ('shopping_cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='digiapp.shoppingcart')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('Good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='digiapp.good')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
                ('reviewer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='digiapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='digiapp.tag'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('Subcategories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='digiapp.subcat')),
            ],
        ),
    ]