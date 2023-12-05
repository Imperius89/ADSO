#se relaiza una corrreccion general de identacion para prevenir errores en la ejecucion del 
def suma(a,b):
      r=(a+b)
      print("Resultado de la suma",r)
def resta(a,b):
      r=(a-b)
      print("Resultado de la resta",r)
def division(a,b):
      r=(a/b)
      print("Resultado de la division",r)
def multiplicacion(a,b):
      r=(a*b)
      print("Resultado de la multiplacion",r)
def potencia(a,b):
      r=(a**b)
      print("Resultado de la potencia",r)
def radicacion(a,b):
      r=(a**(1/b))
      print("Resultado de la radicacion",r)                              
while True:
      try:
            print("INGRESE LOS NUMEROS") #se hace mas comprensible el menu al cambiar la impresion inicial
            c=(int(input("""PRIMER NUMERO:\n"""))) #se complementa agregando los dos puntos y quitando el salto antes de la lectura0
            d=(int(input("""SEGUNDO NUMERO:\n""")))
      except ValueError:
            print("ERROR CON NUMEROS")
            continue
      MENU=input("""SELECCIONE QUE VA A HACER CON LOS NUMEROS
            1. SUMARLOS
            2. RESTARLOS
            3. DIVIDIRLOS
            4. MULTIPLICARLOS
            5. POTENCIARLOS
            6. RADICARLOS
            7. PITAGORAS FELIXIANO\n""") #Se agrega una septima opcion que sera el teorema de pitagoras
      try:
            if MENU =="1":
                  suma(c,d)
            elif MENU =="2":
                  resta(c,d)
            elif MENU =="3":
                  division(c,d)
            elif MENU =="4":
                  multiplicacion(c,d)
            elif MENU =="5":
                  potencia(c,d)
            elif MENU =="6":
                  radicacion(c,d)
            #se anexa el proceso de la 7ma opcion en el cual se calculara el valor de la hipotenusa sin el uso de una funcion
            elif MENU =="7": #si la opcion elegida es 7 se procede a realizar la operacion sin impiirtar librerias adicionales
                  r=(((c*c)+(d*d))**(1/2)) # se realiza el calculo directamente elevando los catetos al cuadrado y radicando el resultado
                  print(r) #se imprime el resultado de la operacion
            # fin del proceso de la 7ma funcion
            else:
                  print("ERROR")
      except ZeroDivisionError:
                  print("ERROR EN LA DIVISION")
              
     