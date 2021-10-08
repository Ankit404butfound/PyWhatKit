import requests

def web_ss(weblink):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    url = weblink
    path = 'me.jpg'
    response = requests.get(BASE + url, stream=True)
    # save file, see https://stackoverflow.com/a/13137873/7665691
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
