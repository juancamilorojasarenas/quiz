
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_gemelos(a, b):
    print("primos gemelos encontrados:")
    for i in range(a, b - 1):  
        if es_primo(i) and es_primo(i + 2): 
            print(f"{i} y {i + 2}")


def es_palindromico(n):
    return str(n) == str(n)[::-1]

def palindromico(a, b):
    print("es un número palindrómico.")
    if b <= a:
        return "El límite superior debe ser mayor que el límite inferior."

    for i in range(a, b + 1):
        if es_palindromico(i):
            print(f"{i} ")

