from django.contrib import admin
from .models import Member, Track, Album, Leader, Gallery, Event, EventGoer
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_filter = ('church','note','residence','age')
    list_display = ('name', 'age','church', 'note', 'residence')
    fields = [('name', 'note'), ('church', 'residence'),
              ('age', 'phone'), 'voice_sample']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_filter = ('album',)
    list_display = ('name', 'album')


class TrackInline(admin.TabularInline):
    model = Track
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_filter = ('producer','release_date')
    list_display = ('name', 'producer','release_date','feature')
    inlines = [TrackInline]


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display=('name','position')
    fields = [('name','position'),'leaders_pic']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_filter = ('event',)
    list_display = ('event','feature')

class EventGoerInline(admin.TabularInline):
    model = EventGoer
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ('location','date')
    list_display = ('title','date','location')
    fields = ['location','date',('start_time','stop_time')]
    inlines = [EventGoerInline]


@admin.register(EventGoer)
class EventGoerAdmin(admin.ModelAdmin):
    list_filter = ('event','age')
    list_display = ('name','age','phone','event')
    fields = [('name','age'),('phone','event')]