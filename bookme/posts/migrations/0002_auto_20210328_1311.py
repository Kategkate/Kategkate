# Generated by Django 2.2.19 on 2021-03-28 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Available'), ('O', 'Occupied')], default='a', help_text='Item availability', max_length=1),
        ),
        migrations.AddField(
            model_name='apartment',
            name='summary',
            field=models.TextField(default=django.utils.timezone.now, help_text='Enter a brief description of the item', max_length=1000),
            preserve_default=False,
        ),
    ]