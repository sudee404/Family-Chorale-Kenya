from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date as dt
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os

def validate_age(value):
    if value > 100:
        raise ValidationError(
            _('Too old to join'),
        )

def validate_pic_size(file):
         if file:
             if file.size > 5*1024*1024:
                   raise ValidationError("File is too large ( > 5mb )")

def validate_audio(file):
         if file:
             if file.size > 50*1024*1024:
                   raise ValidationError("File is too large ( > 50mb )")

             if not os.path.splitext(file.name)[1] in [".mp3",".wav" ,".aac",".MP3",".WAV" ,".AAC"]:
                   raise ValidationError("Audio file has to be an mp3 file")

class Member(models.Model):
    
    name = models.CharField(max_length=255, help_text='Enter your full name',unique=True)
    age = models.PositiveIntegerField(help_text='Enter your age',validators=[validate_age])
    phone = PhoneNumberField()
    church = models.CharField(max_length=255, help_text='Church you belong to')
    note =models.CharField(max_length=255, help_text="Voice note you play")
    residence = models.CharField(max_length=255)
    voice_sample = models.FileField(upload_to='media/sample/',help_text='sample of your voice in aac or mp3 format',null=True)
    
    def get_absolute_url(self):
        return reverse('member-added')
    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, help_text='Enter album name',unique=True)
    producer = models.CharField(max_length=255, help_text='Enter producer\'s name',null=True,default="The Family Chorale")
    release_date = models.DateField()
    album_art = models.ImageField(
        default='media/album_art/default.png', upload_to='media/album_art/',validators=[validate_pic_size])
    detail = models.TextField()
    feature = models.BooleanField(default=False)

    @property
    def featured(self):
        if self.feature:
            return True
        return False

    def get_absolute_url(self):
        return reverse('album-detail',  args=[str(self.id)])

    def __str__(self) -> str:
        return self.name



class Track(models.Model):
    name = models.CharField(max_length=255, help_text="Track's name",unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    link = models.TextField(
        help_text='Enter the youtube video link')
    audio = models.FileField(upload_to='media/audio/',null=True,blank=True,validators=[validate_audio])
    
    def get_absolute_url(self):
        return reverse('track-detail',  args=[str(self.id)])

    def __str__(self) -> str:
        return self.name


class Leader(models.Model):
    name = models.CharField(max_length=255, help_text='Enter your full name',unique=True)
    leaders_pic = models.ImageField(upload_to='media/leaders/' ,default='media/leaders/default.png',validators=[validate_pic_size])
    position = models.CharField(max_length=255, help_text='Hierarchy',null=True)
    
    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200,unique=True)
    poster = models.ImageField(
        upload_to='posters/', default='posters/default.jpeg',validators=[validate_pic_size])
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(null=True)
    stop_time = models.TimeField(null=True)
    location = models.CharField(max_length=200, default='Kisumu')

    @property
    def expired(self):
        if self.date and dt.today() > self.date:
            return True
        return False

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-date']

class Gallery(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE, help_text='Event where picture was taken',null=True)
    picture = models.ImageField(upload_to='media/gallery/',
                                help_text='upload picture',validators=[validate_pic_size],unique=True)
    feature = models.BooleanField(default=False)

    @property
    def featured(self):
        if self.feature:
            return True
        return False

    def __str__(self):
        return self.event.title

class EventGoer(models.Model):
    name = models.CharField(max_length=255, help_text='Enter your full name')
    age = models.PositiveIntegerField(help_text='Enter your age')
    phone = PhoneNumberField()
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True)

    def get_absolute_url(self):
        return reverse('event-booked')
        
    def __str__(self) -> str:
        return self.name