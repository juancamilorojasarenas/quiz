def verificacion_prima(a,b):
    try:
        if b/a==b/2:
            print("los numeros  son primos")
        else:
            print("los numeros no son primos")
    except ZeroDivisionError:
        print("no se puede dividir por cero")

#limite=int(input("por favor ingrese el limite superior: "))
#verificacion_prima(2,limite)

def primos_gemelos(a,b):
    for i in range (a,b+1):
       for j in range (a,b+2):
            if not i/j and i-j==2:
                    print(i,j)


        



        


    

