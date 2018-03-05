from django.shortcuts import render
from lyric_crawler.crawler import search_song, get_lyric

# Create your views here.
def lyric_search(request):
    if 'song' in request.GET and request.GET['song'] != '':
        song_list = search_song(request.GET['song'])
        return render(request, 'lyric_crawler/songs.html', context=locals())
    elif 'link' in request.GET and request.GET['link'] != '':
        song_detail = get_lyric(request.GET['link'])
        return render(request, 'lyric_crawler/lyric.html', context=locals())
    else:
        return render(request, 'lyric_crawler/index.html')