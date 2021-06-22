#only page level editing not text based editing
import PyPDF2,os

from PyPDF2 import pdf
print(os.getcwd())

pdfFile = open('meetingminutes1.pdf','rb')

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page0 = reader.getPage(0)
print(page0.extractText())
