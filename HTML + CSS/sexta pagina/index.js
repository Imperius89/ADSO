var val = 0
var sum = 0

while(val != "acabar") {
    val = prompt("La suma total es: " + sum  + "\nIntroduzca un numero o la palabara 'acabar' ")
    
    if (val!="acabar") {
        var sum = parseInt(sum) + parseInt(val)
    }
}

document.write("Suma total = " + sum + ".")