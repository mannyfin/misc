# from __future__ import unicode_literals
import youtube_dl
from pandas import read_csv
import os



ytl = read_csv('ytlist.csv', sep='\r', header=None)

ytl = [i for j in ytl.values.tolist() for i in j]

os.mkdir('Vamvakaris')
os.chdir('Vamvakaris')

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):

    if d['status'] == 'finished':
        print('Done downloading '+str(d['filename']) + ' of ' + str(len(ytl))+' now converting ...')

# get name w/o yt video id
# for playlists
ydl_opts = {
    # 'playlist_items': '8-10',
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

#
# # get name w/o yt video id
# ydl_opts = {
#     'outtmpl': '%(title)s.%(ext)s',
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#     }],
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
# }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    incr=1
    ydl.download(ytl)

