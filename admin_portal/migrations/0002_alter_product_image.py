# Generated by Django 3.2.9 on 2021-11-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
    ]
