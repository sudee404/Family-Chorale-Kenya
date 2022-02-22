from django.shortcuts import render
from .models import Member,Track,Album,Leader,Gallery,Event,EventGoer
from django.views import generic
from . import forms
# Create your views here.
def index(request):
    events = Event.objects.order_by('-date')
    event1 = Event.objects.order_by('-date')[0]
    album = Album.objects.filter(feature=True)[0]
    context = {
        'events':events,
        'feat_event':event1,
        'album':album,
        
    }
    return render(request,'index.html',context=context)

def gallery(request):
    gallery = Gallery.objects.order_by('event')
    context = {
        'gallery_list':gallery,
        
    }
    return render(request,'family_chorale/gallery_list.html',context=context)

class AlbumListView(generic.ListView):
    model = Album

class AlbumDetailView(generic.DetailView):
    model = Album

class TrackDetailView(generic.DetailView):
    model = Track

class EventListView(generic.ListView):
    model = Event

class LeaderListView(generic.ListView):
    model = Leader

class MemberCreateView(generic.CreateView):
    form_class = forms.MemberForm
    template_name = 'family_chorale/member_form.html'
    success_url = 'success'

class EventGoerCreateView(generic.CreateView):
    model = EventGoer
    fields = '__all__'


class MemberAddedView(generic.TemplateView):
    template_name = 'family_chorale/member_added.html'

class EventBookedView(generic.TemplateView):
    template_name = 'family_chorale/event-booked.html'