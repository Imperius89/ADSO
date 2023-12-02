public class ejercicios{

    public static void main(String[] args) {
        
        int a = 15;
        int b = 23;
        int c = 12;
        
        //Ejercicio 1.

        int Volumen = a * b * c;
        System.out.println("1. El volumen es: " + Volumen);

        //Ejercicio 2.

        int m = 12;
        int v = 3;
        double ec = ((m * Math.pow(v, 2)) / 2);
        System.out.println(String.format("La energia cinetica es:  %.2f", ec));

        //Ejercicio 3:
        
        char aa ='R';
        long ab = 1495970192837664l;
        float ac = 12.5f;
        boolean ad = true;
        int ae = 90;
        String af = "Aca va la frase que no voy a trascribir :D";
        double ag = 6.6268541986d;

        System.out.println("a. La variable: " + aa + " es de tipo: char");
        System.out.println("b. La variable: " + ab + " es de tipo: long");
        System.out.println("c. La variable: " + ac + " es de tipo: float");
        System.out.println("d. La variable: " + ad + " es de tipo: boolean");
        System.out.println("e. La variable: " + ae + " es de tipo: int");
        System.out.println("f. La variable: " + af + " es de tipo: String");
        System.out.println("g. La variable: " + ag + " es de tipo: double");

        //Ejercicio 4:

        double subtotal = (60 * 0.30) + (100 * 0.25) + (20 * 80);
        double iva = subtotal * 0.16;
        double total = subtotal + iva;
        System.out.println(String.format("El valor a pagar es: $ %.2f ", subtotal));
        System.out.println(String.format("El valor con iva incluido a pagar es: $ %.2f ", total));

    }

}