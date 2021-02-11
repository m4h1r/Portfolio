#pip install pdfminer.six
#import libraries
from gtts import gTTS
from playsound import playsound
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
import os

def pdf_to_text(pdfname):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text

#Get all text
all_text = pdf_to_text('book.pdf')
#Split Sentences
sentences = all_text.split(".")

#Read all 
for sentence in sentences:
    cleared_sentence = sentence.strip().replace("\n", " ")+"."
    print(cleared_sentence)
    tts = gTTS(cleared_sentence, lang='tr')
    tts.save("sentence.mp3") #If you have noting to read this code gives error. Use try and except to avoid.
    playsound("sentence.mp3")
    os.remove("sentence.mp3")
