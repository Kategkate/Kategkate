# Generated by Django 2.2.19 on 2021-03-28 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminid', models.AutoField(db_column='AdminID', primary_key=True, serialize=False)),
                ('adminname', models.CharField(db_column='AdminName', default='giru', max_length=50, verbose_name='Name')),
            ],
            options={
                'db_table': 'Admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('host_id', models.AutoField(db_column='Host_ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='First_Name', max_length=30, null=True, verbose_name='First')),
                ('last_name', models.CharField(blank=True, db_column='Last_Name', max_length=30, null=True, verbose_name='Last')),
            ],
            options={
                'db_table': 'Host',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roomtype',
            fields=[
                ('roomtypeid', models.AutoField(db_column='RoomTypeID', primary_key=True, serialize=False)),
                ('roomtype', models.CharField(blank=True, db_column='RoomType', max_length=20, null=True, verbose_name='Type')),
            ],
            options={
                'db_table': 'RoomType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('traveller_id', models.AutoField(db_column='Traveller_ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='First_Name', max_length=30, null=True, verbose_name='First')),
                ('last_name', models.CharField(blank=True, db_column='Last_Name', max_length=30, null=True, verbose_name='Last')),
            ],
            options={
                'db_table': 'Traveller',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('rentid', models.AutoField(db_column='RentID', primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, db_column='Account', max_length=1, null=True)),
                ('from_date', models.DateTimeField(blank=True, db_column='From_Date', null=True, verbose_name='Check-In Date')),
                ('to_date', models.DateTimeField(blank=True, db_column='To_Date', null=True, verbose_name='Check-Out Date')),
                ('isactive', models.NullBooleanField(db_column='ISactive')),
                ('roomtypeid', models.ForeignKey(blank=True, db_column='RoomTypeID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='posts.Roomtype')),
            ],
            options={
                'db_table': 'Rent',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartid', models.AutoField(db_column='apartID', primary_key=True, serialize=False)),
                ('is_reserved', models.NullBooleanField(db_column='IS_Reserved')),
                ('roomtype', models.ForeignKey(db_column='RoomType', on_delete=django.db.models.deletion.DO_NOTHING, to='posts.Roomtype', verbose_name='Room Type')),
            ],
        ),
    ]