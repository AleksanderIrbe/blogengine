# Generated by Django 2.2.2 on 2019-11-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191125_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
