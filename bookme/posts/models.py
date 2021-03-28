from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import CharField
from django.shortcuts import reverse


class Admin(models.Model):
    """
  Model representing the Admin panel
  """

    adminid = models.AutoField(db_column='AdminID', primary_key=True)  # Field name made lowercase.
    adminname = models.CharField(db_column='AdminName', max_length=50, default='giru',
                                 verbose_name='Name')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Admin'


class Host(models.Model):
    """
Model representing the Host of the apartment
"""
    host_id = models.AutoField(db_column='Host_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=30, blank=True, null=True,
                                  verbose_name='First')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=30, blank=True, null=True,
                                 verbose_name='Last')  # Field name made lowercase.
    list_display = ('First_Name', 'Last_Name')

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        managed = True
        db_table = 'Host'


class Traveller(models.Model):
    """
Model representing the Traveller, who is booking this apartment
"""
    traveller_id = models.AutoField(db_column='Traveller_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=30, blank=True, null=True,
                                  verbose_name='First')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=30, blank=True, null=True,
                                 verbose_name='Last')  # Field name made lowercase.
    list_display = ('First_Name', 'Last_Name')

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        managed = True
        db_table = 'Traveller'


class Apartment(models.Model):
    """
    Model representing the Apartment and the options to file different paragraphs
    """

    STATUS_CHOICES = (
        ('A', 'Available'),
        ('O', 'Occupied'),
    )

    ROOM_CHOICES = (
        ('Hotel', 'Hotel'),
        ('Apartment', 'Apartment'),
        ('House', 'House')
    )

    LABEL_CHOICES = (
        ('WA', 'With Amenities'),
        ('SHA', 'Shared Space'),
    )

    apartid = models.AutoField(db_column='apartID', primary_key=True)  # Field name made lowercase.
    roomtype = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomType',
                                 verbose_name='Room Type')  # Field name made lowercase.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the item")
    is_reserved = models.NullBooleanField(db_column='IS_Reserved')  # Field name made lowercase.
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, default='a', help_text='Item '
                                                                                                       'availability')

    class Meta:
        managed = True
        db_table = 'APARTMENT'


class Rent(models.Model):
    rentid = models.AutoField(db_column='RentID', primary_key=True)  # Field name made lowercase.
    roomtypeid = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomTypeID', blank=True, null=True)
    account: CharField = models.CharField(db_column='Account', max_length=1, blank=True, null=True)
    from_date = models.DateTimeField(db_column='From_Date', blank=True, null=True, verbose_name='Check-In Date')
    to_date = models.DateTimeField(db_column='To_Date', blank=True, null=True, verbose_name='Check-Out Date')
    isactive = models.NullBooleanField(db_column='ISactive')

    def __str__(self):
        return self.account

    class Meta:
        managed = True
        db_table = 'Rent'


class Roomtype(models.Model):
    roomtypeid = models.AutoField(db_column='RoomTypeID', primary_key=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=20, blank=True, null=True,
                                verbose_name='Type')  # Field name made lowercase.

    def __str__(self):
        return self.roomtype

    class Meta:
        managed = True
        db_table = 'RoomType'
