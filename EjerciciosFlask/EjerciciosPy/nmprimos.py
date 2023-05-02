#Numeros Primos
def principal(numero):
    n=int(numero)-1
    resultado=0
    primo=True
    try:
            entero=int(numero)
    except ValueError:
            return "El numero debe ser entero"
    while n>1 :
        resultado= int(numero) % n
        if resultado==0 :
            primo=False
            n=0
        else:
            n=n-1    
    if(primo==True):
       return "El numero es primo"       
    else:
        return "El numero no es primo" 
