
#Requisitos

 #Implementar un menú de aplicación con las siguientes opciones:
        #[1] – Importar palabras clave
        #[2] – Mostrar palabras clave
        #[0] – Salir
 #Implementar una función carga_keywords() que lea un fichero llamado keywords.txt:
        #El fichero tendrá una(s) palabra(s) clave por línea.
        #No hay que separar las palabras clave con ningún carácter, solo enter.
        #El fichero se leerá línea a línea, guardando la palabra clave correspondiente como un nuevo elemento de una lista.
        #La función devolverá una lista de palabras clave.

    #Cuando se introduzca la opción de menú [1], se invocará a la función carga_keywords(). La lista resultante se asignará a una variable del programa llamada keywords.
    #Cuando se introduzca la opción de menú [2], se mostrará el listado de palabras clave de 20 en 20, es decir, una vez mostradas 20 palabras clave, el usuario deberá pulsar la tecla enter para ver las siguientes.
    #Cuando se introduzca la opción de menú [0], el programa finalizará.







#Librerias
import os

#variables
keyword = []
opc = 0
cl = lambda: os.system("cls")





while(opc == 0):

        #metodos
        def carga_keywords():
                with open("keywords.txt") as archivo:

                        for line in archivo:
                                #print(line.split())
                                keyword.extend(line.split())

        def mostrar_keywords():
                wordcount = len(keyword)
                contador =0
                contador2= 1
             
                while  contador <=wordcount:
                        if contador == 20*contador2:
                                print("de click en enter para continuar")
                                s=input()
                                contador2 +=1
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
                        opc = 0
                elif(opc =="2"):
                        mostrar_keywords()
                        opc = 0
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





