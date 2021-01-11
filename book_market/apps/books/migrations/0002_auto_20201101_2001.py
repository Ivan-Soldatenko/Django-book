# Generated by Django 3.1.2 on 2020-11-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author_name",
            field=models.CharField(blank=True, default="-", max_length=50),
        ),
        migrations.AlterField(
            model_name="book", name="description", field=models.TextField(default="")
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(default="", max_length=50),
        ),
    ]
