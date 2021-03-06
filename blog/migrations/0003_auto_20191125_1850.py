# Generated by Django 2.2.2 on 2019-11-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191117_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
