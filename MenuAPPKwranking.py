
#Librerias
import os

#variables
keyword = []
opc = 0
cl = lambda: os.system("cls")


#metodos
def carga_keywords():
        with open("keywords.txt") as archivo:

                for line in archivo:
                        print(line.split())
                        keyword.extend(line.split())
                        #print(keyword)
                        return keyword



while(opc == 0):
        try:
                print("******************************************************")
                print("*                      Menu                          *")
                print("******************************************************")
                print("* [1]- Importar palabras clave                       *")
                print("* [2]- Mostrar palabras clave                        *")
                print("* [3]- Salir                                         *")
                print("******************************************************")
                print("* Ingresa una opcion:                                *")
                opc = input()
            
                if(opc == "1"):
                        carga_keywords()
                        print(keyword)
                elif(opc =="2"):
                        print("Opcion ingresada invalida")
                elif(opc =="3"):
                        print("Opcion ingresada invalida")
                else:

                        print("Opcion ingresada invalida")
                        s = input()
                        opc = 0
                        cl()
           


        except EOFError:
                print("Porfavor ingrese una opcion")
                continue





