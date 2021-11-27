from PyPDF2 import PdfFileReader
import os
import sys

    
liste = []

with os.scandir(os.getcwd()) as tarama:
    for belge in tarama:

        if belge.name.endswith(".pdf"): #add to list this extensions
    
            liste.append(belge.name)


toplam = 0
sayac = 0
for i in liste:
    with open(i, "rb") as pdf_file:
        
        if not sys.warnoptions: #warning uyarısı prevented
            import warnings
            warnings.simplefilter("ignore")
            
        sayac+=1
        pdf_reader = PdfFileReader(pdf_file)
        print(f"{sayac} - {i} named file page number: \n {pdf_reader.numPages}")
        toplam = toplam + int(pdf_reader.numPages)

print(f"Total page number : {toplam}")

girdi = input("enter for quit")
if (girdi == True):
    quit()
