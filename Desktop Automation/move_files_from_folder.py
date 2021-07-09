import os
import shutil

os.chdir('C:\\Users\\sai\\Desktop\\Viraj\\Hindi & Other Songs')

files = os.listdir()

source = 'C:\\Users\\sai\\Desktop\\Viraj\\Hindi & Other Songs\\'

for f in files :
    os.chdir('C:\\Users\\sai\\Desktop\\Viraj\\Hindi & Other Songs\\{}'.format(f))
    songs = os.listdir()
    print(songs)

    for song in songs:
      print(song)
      shutil.move(source+'\\'+f+'\\'+song,source)
