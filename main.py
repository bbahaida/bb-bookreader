import pyttsx3
import PyPDF2
# r'C:\Users\Admin\Downloads\hashcode_2020_online_qualification_round.pdf'
path = str(input("Enter the book full path: "))
lang = str(input("Enter the book language(fr, en): ")).lower()
start = int(input("starting page: ")) - 1
end = int(input("end page: ")) - 1
book = open(path, 'rb')
engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices')
if lang == 'fr':
    engine.setProperty('voice', voices[0].id)

if lang == 'en':
    engine.setProperty('voice', voices[2].id)

engine.setProperty('rate', 140)
pdfReader = PyPDF2.PdfFileReader(book)
for num in range(start, end):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()

