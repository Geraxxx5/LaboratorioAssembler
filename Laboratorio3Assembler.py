#Programacion Laboratorio 3
#Diego Garcia
#Gerardo Pineda
def nBinario():
    binarioSigno = input("Ingrese un numero binario con signo de 8 bits:\n")
    print("---------------------------")

    if(len(binarioSigno) != 8):
        print("El numero binario ingresado es menor o mayor a 8 bits")
    else:
        if(binarioSigno.isdigit()):
            flag = True
            A1 = []
            A2 = []
            for character in binarioSigno:
                if(character == "1" or character == "0"):
                    if(character == "1"):
                        character = 0
                    else:
                        character = 1
                    A1.append(character)
                    A2.append(character)
                else:
                    flag = False
            
            if(flag):
                bA1 = ""
                for x in A1:
                    bA1+=str(x)
                print("Binario: "+binarioSigno)
                print("A1: "+bA1)            
                if((A2[-1] + 1)>1):
                    primerCero = True
                    pos = 0
                    for i in range(1,9):
                        if(primerCero):
                            if(A2[-i] == 0):
                                A2[-i] = 1
                                primerCero = False
                            else:
                                A2[-i] = 0
                    
                    bA2 = ""
                    for x in A2:
                        bA2+=str(x)

                    if(primerCero):
                        print("A2: 1|"+bA2+" Overflow del numero")
                    else:
                        print("A2: "+bA2)                   
                else:
                    A2[-1] = A2[-1]+1
                    bA2 = ""
                    for x in A2:
                        bA2+=str(x)
                    print("A2: "+bA2) 
            
            else:
                print("No es un numero binario")
    print("---------------------------")


def hexadec():
    menu = input("Selecciona la opcion que dese:\n1) Hexadecimal de 3 digitos a decimal\n2) Decimal a hexadecimal: \n")
    cHexadecimal = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }
    if(menu == "1"):
        hexadecimal = input("Ingrese el un numero hexadecimal de 3 digitos:\n")
        valores = list(cHexadecimal.values())
        llaves = list(cHexadecimal.keys())
        if(len(hexadecimal) <= 3):
            validar = True
            resultado = 0
            if(len(hexadecimal) == 1):
                contPower = 0
            elif(len(hexadecimal) == 2):
                contPower = 1
            else:
                contPower = 2
            for x in hexadecimal:
                if(not (x.upper() in valores)):
                    validar = False
                else:
                    pos = valores.index(x.upper())
                    resultado+= llaves[pos]*pow(16,contPower)
                    contPower-=1
            if(validar):
                print(resultado)
            else:
                print("Caracter no valido para hexadecimal")
        else:
            print("Unicamente hexadecimal de 3 digitos")
        
    if(menu == "2"):
        hexadecimal = input("Ingrese un numero entero y positivo, que se pueda representar en 3 hexadecimales:\n")
        if(hexadecimal.isdigit() and int(hexadecimal) >= 0 and int(hexadecimal) <= 4095):
            restos = []
            listo = True
            hexadecimal = int(hexadecimal)
            dividiendo = hexadecimal
            while listo:
                resultado = dividiendo//16 
                restos.append(dividiendo-(resultado*16))
                dividiendo = resultado
                if(dividiendo == 0):
                    listo = False
                
            respuesta = ""
            for i in range(1,(len(restos)+1)):
                respuesta+=str(cHexadecimal[restos[-i]])
            
            print("Hexadecimal: "+respuesta)

                
        else:
            print("Ingrese unicamente un numero entero positivo y que se puede representar en 3 hexadecimales")

print("Bienvenido al programa")
bandera = True
while bandera:
    opc = input("Seleccione la opcion que desea:\n1) Programa 1 Binario\n2) Programa 2 hexadecimal\n3) salir\n")
    if(opc == "1"):
        nBinario()
    elif(opc == "3"):
        bandera = False
    else:
        hexadec()

