import os
import shutil

EXT_ZIP = ['.tar','.7z','.dmg','.rar','.zip']
EXT_EXECUTAILBE = ['.exe','.bat','.gadget','.apk','.jar','.']
EXT_AUDIO = ['.cda','.mp3','.midi','.wav','.m3u','.wma','.ogg','.mpa','.mid']
EXT_VIDEO = ['.avi','.flv','.m4v','.mp4','.mkv','.mpg','.mpeg','.wmv']
EXT_IMAGES = ['.ai','.bmp','.jpg','.jpeg','.png','.ps','.psd','.svg','.tif','.tiff','.JPG']
EXT_TEXT = ['.txt','.pdf','.doc','.docx']
EXT_CODING = ['.c','.class','.java','.js','.py','.html','.pde','.json','.htm','.xml','.log','.tar','.sql','.sh','.h']
EXT_FONT = ['.fnt','.fon','.ttf','.otf']
EXT_PRESENTATION = ['.key','.odp','.pps','.ppt','.pptx']
EXT_SPREADSHEET = ['.ods','.xlr','.xls','.xlsx']
EXT_SYSTEM = ['.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp']

os.chdir('C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test')

print("Downlaods Folder Cleanup")
print('Current Dir : {}'.format(os.getcwd()))
print()

files = os.listdir()

DIRS = ['Audio','Video','Images','Text','Folder','Other','Coding','Executables','Zip','Font','Presentation','Spreadsheet','System']

#if os.getcwd() !=  os.path.isdir('./Audio'):
#    for d in DIRS :
#        os.mkdir('.{}'.format(d))
#    print('Directories created Successfully')

for f in files :
    name, extension = os.path.splitext(f)

    if extension in EXT_IMAGES :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\new folder\\.Images'
        shutil.move(source,destination)
    elif extension in EXT_EXECUTAILBE :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Executaibles'
        shutil.move(source,destination)
    elif extension in EXT_AUDIO :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Audio'
        shutil.move(source,destination)
    elif extension in EXT_CODING :
        source = 'C:\\Users\\vlbha\\Desktop\\new folder\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Coding'
        shutil.move(source,destination)        
    elif extension in EXT_TEXT :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\new folder\\.Text'
        shutil.move(source,destination)
    elif extension in EXT_VIDEO :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Video'
        shutil.move(source,destination)
    elif extension in EXT_VIDEO :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Zip'
        shutil.move(source,destination)
    elif extension in EXT_FONT :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Font'
        shutil.move(source,destination)
    elif extension in EXT_PRESENTATION :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Presentation'
        shutil.move(source,destination)
    elif extension in EXT_SPREADSHEET :
        source = 'C:\\Users\\vlbha\\Desktop\\new folder\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\new folder\\.Spreadsheet'
        shutil.move(source,destination)
    elif extension in EXT_SYSTEM :
        source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
        destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.System'
        shutil.move(source,destination)
    """
    else :
        if os.path.isdir(name):
            if name not in DIRS:
                source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
                destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Folder'
                shutil.move(source,destination)
        else :
            source = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\{}{}'.format(name,extension)
            destination = 'C:\\Users\\vlbha\\Desktop\\Code\\Python\\Desktop Automation\\Test\\.Other'
            shutil.move(source,destination)
    """
#Extensions
extension_paths = {
        # No name
        'noname':  'other/uncategorized',
        # audio
        '.aif':    'media/audio',
        '.cda':    'media/audio',
        '.mid':    'media/audio',
        '.midi':   'media/audio',
        '.mp3':    'media/audio',
        '.mpa':    'media/audio',
        '.ogg':    'media/audio',
        '.wav':    'media/audio',
        '.wma':    'media/audio',
        '.wpl':    'media/audio',
        '.m3u':    'media/audio',
        # text
        '.txt':    'text/text_files',
        '.doc':    'text/microsoft/word',
        '.docx':   'text/microsoft/word',
        '.odt ':   'text/text_files',
        '.pdf':    'text/pdf',
        '.rtf':    'text/text_files',
        '.tex':    'text/text_files',
        '.wks ':   'text/text_files',
        '.wps':    'text/text_files',
        '.wpd':    'text/text_files',
        # video
        '.3g2':    'media/video',
        '.3gp':    'media/video',
        '.avi':    'media/video',
        '.flv':    'media/video',
        '.h264':   'media/video',
        '.m4v':    'media/video',
        '.mkv':    'media/video',
        '.mov':    'media/video',
        '.mp4':    'media/video',
        '.mpg':    'media/video',
        '.mpeg':   'media/video',
        '.rm':     'media/video',
        '.swf':    'media/video',
        '.vob':    'media/video',
        '.wmv':    'media/video',
        # images
        '.ai':     'media/images',
        '.bmp':    'media/images',
        '.gif':    'media/images',
        '.jpg':    'media/images',
        '.jpeg':   'media/images',
        '.png':    'media/images',
        '.ps':     'media/images',
        '.psd':    'media/images',
        '.svg':    'media/images',
        '.tif':    'media/images',
        '.tiff':   'media/images',
        '.cr2':    'media/images',
        # internet
        '.asp':    'other/internet',
        '.aspx':   'other/internet',
        '.cer':    'other/internet',
        '.cfm':    'other/internet',
        '.cgi':    'other/internet',
        '.pl':     'other/internet',
        '.css':    'other/internet',
        '.htm':    'other/internet',
        '.js':     'other/internet',
        '.jsp':    'other/internet',
        '.part':   'other/internet',
        '.php':    'other/internet',
        '.rss':    'other/internet',
        '.xhtml':  'other/internet',
        '.html':   'other/internet',
        # compressed
        '.7z':     'other/compressed',
        '.arj':    'other/compressed',
        '.deb':    'other/compressed',
        '.pkg':    'other/compressed',
        '.rar':    'other/compressed',
        '.rpm':    'other/compressed',
        '.tar.gz': 'other/compressed',
        '.z':      'other/compressed',
        '.zip':    'other/compressed',
        # disc
        '.bin':    'other/disc',
        '.dmg':    'other/disc',
        '.iso':    'other/disc',
        '.toast':  'other/disc',
        '.vcd':    'other/disc',
        # data
        '.csv':    'programming/database',
        '.dat':    'programming/database',
        '.db':     'programming/database',
        '.dbf':    'programming/database',
        '.log':    'programming/database',
        '.mdb':    'programming/database',
        '.sav':    'programming/database',
        '.sql':    'programming/database',
        '.tar':    'programming/database',
        '.xml':    'programming/database',
        '.json':   'programming/database',
        # executables
        '.apk':    'other/executables',
        '.bat':    'other/executables',
        '.com':    'other/executables',
        '.exe':    'other/executables',
        '.gadget': 'other/executables',
        '.jar':    'other/executables',
        '.wsf':    'other/executables',
        # fonts
        '.fnt':    'other/fonts',
        '.fon':    'other/fonts',
        '.otf':    'other/fonts',
        '.ttf':    'other/fonts',
        # presentations
        '.key':    'text/presentations',
        '.odp':    'text/presentations',
        '.pps':    'text/presentations',
        '.ppt':    'text/presentations',
        '.pptx':   'text/presentations',
        # programming
        '.c':      'programming/c&c++',
        '.class':  'programming/java',
        '.java':   'programming/java',
        '.py':     'programming/python',
        '.sh':     'programming/shell',
        '.h':      'programming/c&c++',
        # spreadsheets
        '.ods':    'text/microsoft/excel',
        '.xlr':    'text/microsoft/excel',
        '.xls':    'text/microsoft/excel',
        '.xlsx':   'text/microsoft/excel',
        # system
        '.bak':    'text/other/system',
        '.cab':    'text/other/system',
        '.cfg':    'text/other/system',
        '.cpl':    'text/other/system',
        '.cur':    'text/other/system',
        '.dll':    'text/other/system',
        '.dmp':    'text/other/system',
        '.drv':    'text/other/system',
        '.icns':   'text/other/system',
        '.ico':    'text/other/system',
        '.ini':    'text/other/system',
        '.lnk':    'text/other/system',
        '.msi':    'text/other/system',
        '.sys':    'text/other/system',
        '.tmp':    'text/other/system'
        }