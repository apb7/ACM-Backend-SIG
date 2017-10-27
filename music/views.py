from django.shortcuts import render,get_object_or_404
from .models import Album,Song
from django.http import Http404
def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    context={
        'all_albums':all_albums,
    }
    return render(request,'music/index.html',context)
def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    
