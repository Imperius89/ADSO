#edad
edad= int(input("Digite la edad\n"))
# print(edad)
if edad<=0:
    print("La edad no puede ser menor a 0")
elif edad>0 and edad<18:
    print("Eres menor de edad")
elif edad>=18 and edad<45:
    print("Eres mayor de edad")
elif edad>=45 and edad<100:
    print("Eres MUY mayor de edad")
elif edad>=100 and edad<120:
    print("nivel matusalen desbloqueado")
else:
    print("La edad no puede ser mayor a 120")
