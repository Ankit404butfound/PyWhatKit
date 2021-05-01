import PyPDF2
from gtts import gTTS


def create_audiobook(path, name='pywhatkit_audio_book'):

    try:
        book = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
    except:
        raise Exception("couldn't open pdf file")
    for num in range(pages):
        page = pdfReader.getPage(num)
        txt = page.extractText()
        book_ = gTTS(text=txt, slow=False)
        book_.save(f'{name}.mp3')
