from django.shortcuts import render, get_object_or_404
from .models import Song, Book, Story

def home(request):
    latest_songs = Song.objects.all()[:6]  # Get 6 latest songs
    latest_books = Book.objects.all()[:4]  # Get 4 latest books
    return render(request, 'home.html', {
        'latest_songs': latest_songs,
        'latest_books': latest_books
    })
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song/list.html', {'songs': songs})

def song_detail(request, id):
    song = get_object_or_404(Song, id=id)
    return render(request, 'song/detail.html', {'song': song})