public class formas_string{
    public static void main(String[] args) {
        
        int edad = 33;
        float altura = 1.76f;
        double pi = 3.1415789876;
        long distancia = 31516781561849876l;
        boolean bool = true;
        char inicial = 'O';

        System.out.println(String.format("Mi edad es : %d %d", edad, distancia));
        System.out.println("Mi altura es " + altura);
        System.out.println(String.format("Mi altura es %.4f", pi));

    }
}