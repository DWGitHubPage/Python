#Python3.7.3
#Extracting info. from a pdf.

import PyPDF2 
  
pdfFileObj = open('meetingminutes.pdf', 'rb') 
  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
print(pdfReader.numPages) 
  
pageObj = pdfReader.getPage(0) 
  
print(pageObj.extractText())
print("Number of pages: " + str(pdfReader.numPages))
  
pdfFileObj.close() 
