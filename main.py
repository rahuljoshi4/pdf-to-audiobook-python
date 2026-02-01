import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

voice = pyttsx3.init()

volume = int(input("Set a volume from 0 to 10: "))
voice.setProperty('volume', volume/10)

rate = input("Set speaking rate from 0 to 100: ")
voice.setProperty('rate', rate)

gender = input("Male or Female speaking voice?: ")

if gender.lower() == "male":
    voice.setProperty("voice", 1)
else:
    voice.setProperty("voice", 0)


for num in range(0, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    voice.say(text)
    voice.runAndWait()