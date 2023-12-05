
#El vendedor 
#print("Ingrese el dinero del comprador")
c= int(input("Ingrese el dinero del comprador"))

if c == 25:
    print("Pago el precio exacto, no hay vueltos")
elif c > 25:
    #print("Ingrese la cantidad de libros a comprar")
    d= int(input("Ingrese la cantidad de libros a comprar"))
    precio= (d*25)
    if precio < c:
        vueltas= (c-precio)
        print("Hay que darle ",vueltas," de cambio")
    else:
        print("No le alcanzan las lucas :) ")
    
else:
    print("No le alcanzan las lucas lok :) ")
