import os
from PyPDF2 import PdfFileReader as pdf_reader
import pandas as pd
from time import *
print("Este Programa Sirve para saber la sumatoria de pagians de un pdf")
print("Nota: Nesesita Estar en una carpeta donde solo se encuentre Este Scripts y Pdfs")

print("")
print("")
print("")
print("")


myList=os.listdir()
print(len(myList))
x= len(myList)-1
#print(x)


posicion = x 
if(int(posicion) <= len(myList)):
    myList.pop(int(posicion))
    
    
#print(len(myList))

    
for x in myList:
    print(str(x)+"  "+str(pdf_reader(x).getNumPages()))

numPages=0
for x in myList:
    numPages=numPages+pdf_reader(x).getNumPages()
    


print("Numero de Paginas en esta Carpeta:      "+str(numPages))

input('Enter para finalizar')
