from PyPDF2 import PdfFileReader
import os
import sys

    
liste = []

with os.scandir(os.getcwd()) as scann:
    for docm in scann:

        if docm.name.endswith(".pdf"): #add to list this extensions
    
            liste.append(docm.name)


total = 0
countr = 0
for i in liste:
    with open(i, "rb") as pdf_file:
        
        if not sys.warnoptions: #warning prevented
            import warnings
            warnings.simplefilter("ignore")
            
        countr+=1
        try:
            pdf_reader = PdfFileReader(pdf_file)
            print(f"{countr} - Number of pages in file {i}: {pdf_reader.numPages} \n")
            total = total + int(pdf_reader.numPages)
        except:
            print(f"{countr} - There is a problem with file {i}, pdf cannot be resolved \n")

print(f"Total page number : {total}")

oinput = input("enter for quit")
if (oinput == True):
    quit()
