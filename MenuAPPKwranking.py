import os

opc = 0
cl = lambda: os.system("cls")


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
            if(opc !="1" or opc !="2" or opc !="3"):
                
                print("Opcion ingresada invalida")
                s = input()
                opc = 0
                cl()
           


        except EOFError:
                print("Porfavor ingrese una opcion")
                continue

