# Generated by Django 2.2.19 on 2021-04-07 13:16

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]