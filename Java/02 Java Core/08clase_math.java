public class clase_math{

    public static void main(String[] args) {
        
        int a = 15;
        int b = 8;
        
        //Area

        int Area = b * a;

        //Perimetro

        int Perimetro = (2 * a ) + (2 * b);

        //Triangulo 

        double triangulo = ((a*b)/2);

        System.out.println("El areas es: " + Area + " El perimetro es: " + Perimetro + " El triangulo es: " + triangulo);

        //Circulo

        int r = 60;

        // Area del circulo

        double pi = 3.1416;
        double cArea = pi * Math.pow(r,2);

        System.out.println(cArea);

        //Hypotenusa

        a = 5;
        b = 3;

        double sumaCatetos = Math.pow(a, 2) +Math.pow(b, 2);
        double Area2 = Math.sqrt(sumaCatetos);

        System.out.println(Area2);

        double Area3 = Math.hypot(a,b);

        System.out.println("El directo es este: " + Area3);



    }

}