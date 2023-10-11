import java.util.Arrays;
import java.util.Scanner;
import java.util.Locale;
public class Ej2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
       int[][] matrizA = new int [3][3];
       int[][] matrizB = new int [3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print("Valor en la posición (" + i + ", " + j + "): De la matriz A ");
                matrizA[i][j] = scanner.nextInt();
                System.out.print("Valor en la posición (" + i + ", " + j + "): De la matriz B ");
                matrizB[i][j] = scanner.nextInt();
            }
        }
        int[][] resultado = new int[3][3];
       for (int i = 0; i < 3; i++){
           for (int j = 0; j < 3; j++){
               resultado[i][j] += matrizA[i][j] * matrizB[i][j];

    }
}
        System.out.println("La matriz resultante es igual a:");
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                System.out.print(resultado[i][j] + "\t");

            }
            System.out.println();
        }
}
}