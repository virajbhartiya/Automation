import os
import shutil

os.chdir('C:\\Users\\Dhruv Bhartiya\\Desktop\\viraj\\music')

print("Downlaods Folder Cleanup")
print('Current Dir : {}'.format(os.getcwd()))
print()

files = os.listdir()

for f in files:
  name, extension = os.path.splitext(f)

  if extension == '.m4a':
    os.rename(name+extension, name+'.mp3')
  
files = os.listdir()
print(files)