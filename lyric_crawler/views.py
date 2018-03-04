from django.shortcuts import render
from lyric_crawler.crawler import search_song, get_lyric

# Create your views here.
def index(request):
    if 'song' in request.GET and request.GET['song'] != '':
        song_list = search_song(request.GET['song'])
        print(song_list)
        return render(request, 'lyric_crawler/songs.html', context=locals())
    else:
        return render(request, 'lyric_crawler/index.html')

def search_result(request):
    pass
