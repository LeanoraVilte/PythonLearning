import PyPDF2

pdf = open('WPS.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdf)

page_one = pdfReader.getPage(1)

print(page_one.extractText())