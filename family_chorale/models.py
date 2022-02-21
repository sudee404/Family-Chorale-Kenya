from django.db import models
from django.urls import reverse,reverse_lazy
from datetime import date as dt



class Member(models.Model):
    name = models.CharField(max_length=255, help_text='Enter your full name')
    age = models.PositiveIntegerField(help_text='Enter your age')
    phone = models.CharField(
        max_length=10, help_text='Enter a number beginning with 07')
    church = models.CharField(max_length=255, help_text='Church you belong to',null=True)
    note =models.CharField(max_length=255, help_text="Voice note you play")
    residence = models.CharField(max_length=255,null=True)
    voice_sample = models.FileField(upload_to='media/sample/',null=True,help_text='sample of your voice')
    
    def get_absolute_url(self):
        return reverse('member-added')
    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, help_text='Enter album name')
    producer = models.CharField(max_length=255, help_text='Enter producer\'s name',null=True,default="The Family Chorale")
    release_date = models.DateField()
    album_art = models.ImageField(
        default='media/album_art/default.png', upload_to='media/album_art/')
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
    name = models.CharField(max_length=255, help_text="Track's name")
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    link = models.TextField(
        help_text='Enter the youtube video link')
    audio = models.FileField(upload_to='media/audio/',null=True,blank=True)
    
    def get_absolute_url(self):
        return reverse('track-detail',  args=[str(self.id)])

    def __str__(self) -> str:
        return self.name


class Leader(models.Model):
    name = models.CharField(max_length=255, help_text='Enter your full name')
    leaders_pic = models.ImageField(upload_to='media/leaders/' ,default='media/leaders/default.png')
    position = models.CharField(max_length=255, help_text='Hierarchy',null=True)
    
    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(
        upload_to='posters/', default='posters/default.jpeg')
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
                                help_text='upload picture')
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
    phone = models.CharField(
        max_length=10, help_text='Enter a number beginning with 07',unique=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True)

    def get_absolute_url(self):
        return reverse('member-added')
        
    def __str__(self) -> str:
        return self.name