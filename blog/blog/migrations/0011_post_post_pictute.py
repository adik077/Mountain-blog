# Generated by Django 3.2.5 on 2021-08-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_is_highlited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pictute',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]