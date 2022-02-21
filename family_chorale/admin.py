from django.contrib import admin
from .models import Member,Track,Album,Leader,Gallery,Event,EventGoer
# Register your models here.
admin.site.register(Member)
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Leader)
admin.site.register(Gallery)
admin.site.register(Event)
admin.site.register(EventGoer)