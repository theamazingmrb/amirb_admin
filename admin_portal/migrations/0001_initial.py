# Generated by Django 3.2.9 on 2021-11-24 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField()),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.CharField(max_length=50)),
                ('catagory', models.CharField(max_length=25)),
            ],
        ),
    ]