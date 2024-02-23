import requests #pip install requests
import zipfile
import os
import yt_dlp as youtube_dl # pip install yt-dlp
import time

def playonyt_stream(search):
    '''
    Used to play music in youtube without opening the browser(plays song in python console) and without downloading the song/ytvideo(streaming).
    Automatically install vlc media player in current working directory if it is not present in C:\Program Files\VideoLAN\VLC.

    Ignore the libvlc errors if it occurs
    '''
    try:
        os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
        import vlc #pip install python-vlc
    except:
        if "VLC" in os.listdir():
            os.add_dll_directory(f'{os.getcwd()}\\VLC')
            import vlc
        else:
            print('VLC media player not installed, Installing It.....')
            param_dict = {
                "id": "19mwPKY0LTkJ4I_p6j__cijSIcppzPDLX",
                "export": "download",
                "authuser": "1",
                "confirm": "t",
                "uuid": "aedd8891-820d-4990-a09d-dc4f055505ff",
                "at": "APZUnTUN6UOl55PNEU-BKds63wLx:1708498961088",
            }
            r_obj = requests.get('https://drive.usercontent.google.com/download', params=param_dict)
            with open('VLC.zip', 'wb') as f:
                f.write(r_obj.content)
                f.close()

            with zipfile.ZipFile("VLC.zip", "r") as zip_ref:
                zip_ref.extractall()
            
            os.remove('VLC.zip')

            os.add_dll_directory(f'{os.getcwd()}\\VLC')
            import vlc

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    s = str(search)
    url = f"https://www.youtube.com/results?q={s}"
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/results":
        return None
        
    link = f"https://www.youtube.com{lst[count - 5]}"

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info = ydl.extract_info(link, download=False)
    url = info['url']
    duration = info['duration']

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    time.sleep(duration)
