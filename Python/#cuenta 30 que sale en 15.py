#cuenta 30 que sale en 15
x=0
while (x<30):
    if (x==15):
        print("Se rompio la ejecucion del bucle cuando x vaila ",x)
        break
    elif (x==4) or (x==6) or (x==10):
        print("se salto el valor ",x,"de x")
        pass
    else:
       print(x)
    x=x+1