from utilidades import primos_gemelos, palindromico
menu_principal="""
*****************************************
bienvenido usuari@ presione
1. para encontrar pares de primos gemelos
2. para encontar numeros primos palindromicos
3. para salir del programa
*****************************************

"""

def menu():

    while True:
        print(menu_principal)
        opc=input("ingresa tu opcion: ")
        if opc=="1":
            limite = int(input("Por favor ingrese el límite superior: "))
            primos_gemelos(2,limite)
        elif opc=="2":
            limite = int(input("Por favor ingrese el límite superior: "))
            palindromico(2, limite)
        elif opc=="3":
            print("saliendo....")
            break
        else:
            print("opcion no valida lea bien ")
