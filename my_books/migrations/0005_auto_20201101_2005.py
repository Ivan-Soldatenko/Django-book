# Generated by Django 3.1.2 on 2020-11-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_books', '0004_auto_20201101_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(blank=True, default='unknown author', max_length=50),
        ),
    ]
