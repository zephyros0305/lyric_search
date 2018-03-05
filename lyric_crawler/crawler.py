import requests
import urllib.parse
import re
from bs4 import BeautifulSoup

URL_ROOT = 'http://mojim.com/'

def search_song(song_name):
    
    song_name += '.html?t3'
    url = urllib.parse.urljoin(URL_ROOT, song_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    songs = soup.find_all('dd', re.compile('^mxsh_dd'))
    del songs[0]
    song_list = list()

    for song in songs:
        meta = song.find('span', 'mxsh_ss4').find('a')
        name_temp = meta.getText().split('.')
        song_list.append({
            'name':name_temp[1],
            'singer':song.find('span', 'mxsh_ss2').getText(),
            'album':song.find('span', 'mxsh_ss3').getText(),
            'link':meta.get('href'),
            })

    return song_list

def get_lyric(url):
    url = urllib.parse.urljoin(URL_ROOT, url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    lyric = soup.find('dl', 'fsZx1')

    a = re.compile('^\[\d+')

    lyric_list = list()
    for string in lyric.stripped_strings:
        if string == '更多更詳盡歌詞 在' or string == '※ Mojim.com　魔鏡歌詞網':
            continue
        if a.match(string):
            break
        lyric_list.append(string)

    singer = lyric_list.pop(0)
    name = lyric_list.pop(0)

    song_detail = {
        'singer':singer,
        'name':name,
        'lyric':lyric_list,
    }
    return song_detail