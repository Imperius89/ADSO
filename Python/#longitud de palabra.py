#longitud de palabra
Palabras=["Peine","Pelo","Ventana","Refrigerador","Adolescente","Dentista","Asesino"]
for n in Palabras:
    print(n, "Longitud ", len(n))

a= "-"
x=a.join(Palabras)
print(x, "Longitud ", len(x))

Agenda={
    "Marcelo":"3443456901",
    "Gaston":"3443456902",
    "Lucas":"3443456903",
    "Angela":"3443456904",
    "Lucio":"3443456905",
}
for (x,y) in Agenda.items():
    print ("El valor de la clave es: ", x, " y el valor es: ",y)

l=input("Ingrese la letra a buscar")
entrada="hola estoy programando en python"
cont=0
for n in entrada:
    if (n==l):
        cont=cont+1
print(l,":",cont)
