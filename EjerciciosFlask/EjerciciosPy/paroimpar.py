def parImpar(numero):
    try:

        num = int(numero)
        if num % 2 == 0:
            return f" El número {num} es par"
        else:
            return f" El número {num} es impar"
        
    except:
        return "Error, introduce un número"