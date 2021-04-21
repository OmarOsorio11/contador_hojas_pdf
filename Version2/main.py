#Version 2
import os
from PyPDF2 import PdfFileReader as pdf_reader
import pandas as pd
from time import *
if __name__ == '__main__':
    try:
        print("Este Programa Sirve para saber la sumatoria de pagians de un pdf")
        print("Nota: Pegar en la carpeta PDFS los archivos a contar")

        print("")
        print("")
        print("")
        print("")


        myList=os.listdir("./PDFS")
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


    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print("Press Enter to continue ...")
        input()
