# Generated by Django 3.2.5 on 2021-08-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='gory', max_length=60),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=60),
        ),
    ]
