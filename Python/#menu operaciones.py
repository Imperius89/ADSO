#menu operaciones
def suma(a,b):
    x = a + b
    print("El resultado de la suma es: \n", x)
def resta(a,b):
    x = a - b
    print("El resultado de la resta es: \n", x)
def multi(a,b):
    x = a * b
    print("El resultado de la multiplicacion es: \n", x)
def div(a,b):
    x = a / b
    print("El resultado de la division es: \n", x)
def expo(a,b):
    x = a ** b
    print("El resultado de la exponenciacion es: \n", x)
def radi(a,b):
    x = a ** (1/b)
    print("El resultado de la radicacion es: \n", x)

while True:
    try:
        print(""" 
            Ingrese el numero de la operacion que desea realizar: 
        1.Suma
        2.Resta
        3.Multiplicacion
        4.Division
        5.Exponenciacion
        6.Radicacion """)
        n=int(input())
        a=int(input("Ingrese el primer valor: \n"))
        b=int(input("Ingrese el segundo valor: \n"))
    except (ValueError):
        print("Numero no valido: \n")
        continue
    
    if (n==1):
        suma(a,b)
    elif (n==2):
        resta(a,b)
    elif (n==3):
        multi(a,b)
    elif (n==4):
        try:
            div(a,b)
        except (ZeroDivisionError):
            print("No se puede dividir entre cero mi ciela")
    elif (n==5):
        expo (a,b)
    elif (n==6):
        radi (a,b)
    else:
        print("Todo melo, que mass quiere hacer ñeñe? \n")
        