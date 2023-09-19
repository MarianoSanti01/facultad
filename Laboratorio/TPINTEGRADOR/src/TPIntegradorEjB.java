import java.util.Scanner;
public class TPIntegradorEjB {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Ingrese un numero entero de tres cifras para determinar si es capicua o no");
        int num = scan.nextInt();
        if (num >= 100 && num <= 999) {
            int digito1 = num / 100;
            int digito3 = num % 10;

            if (digito1 == digito3) {
                System.out.println("El número " + num + " es capicúa.");
            } else {
                System.out.println("El número " + num + " no es capicúa.");
            }
        } else {
            System.out.println("El número introducido no es de tres cifras.");
        }
    }
}
