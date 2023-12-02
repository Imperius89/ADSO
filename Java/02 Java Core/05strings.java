public class strings{
    public static void main(String[] args) {
        String saludo = "Estas son las variables";
        int longitud = saludo.length();
        char myChar = saludo.charAt(2);
        boolean stringVacio = saludo.isEmpty();
        boolean containsString = saludo.contains("var");
        String substring = saludo.substring(2, 7);
        String newString = saludo.replace("0", "5");
        
        
        System.out.println(saludo + " (" + longitud + ") " + myChar + " " + substring + " " + newString + " ");

        int edad = 33;
        System.out.println("Mi edad es : " + edad);
        
        float altura = 1.76f;
        System.out.println("Mi altura es: " + altura);

        double pi = 3.1415789876;
        System.out.println("El valor de Pi es: " + pi);

        long distancia = 31516781561849876l;
        System.out.println("El numero largo es: " + distancia);

        boolean bool = true;
        System.out.println("El apuntador esta en: " + bool);

        char inicial = 'O';
        System.out.println("mi inicial es: " + inicial);

    }
}