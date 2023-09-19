import java.util.Scanner;

public class TpIntegradorEjA {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Ingrese un numero entero y luego otro, el programa se encargará de ver si su ultimo valor coincide");
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        if(num1%10 == num2%10){
            System.out.println("El ultimo valor es igual");
        }else{
            System.out.println("Los valores finales no son iguales");}
    }
}