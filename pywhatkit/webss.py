import requests
def web_ss(weblink):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    url = weblink #enters website to be screenshotted
    path = 'me.jpg' #image name is saved as
    response = requests.get(BASE + url, stream=True)# uses requests to complete action

    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
