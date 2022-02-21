from django.urls import path
from . import views

urlpatterns = [
    path('gallery/',views.gallery,name='gallery'),
    path('albums/',views.AlbumListView.as_view(),name='music'),
    path('albums/<int:pk>/',views.AlbumDetailView.as_view(),name='album-detail'),
    path('events/',views.EventListView.as_view(),name='events'),
    path('leaders/',views.LeaderListView.as_view(),name='leaders'),
    path('track/<int:pk>/',views.TrackDetailView.as_view(),name='track-detail'),
    path('become-a-member/',views.MemberCreateView.as_view(),name='member-add'),
    path('attend-event/',views.EventGoerCreateView.as_view(),name='attend'),
]
