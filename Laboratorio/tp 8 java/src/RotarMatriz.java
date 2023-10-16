public class RotarMatriz {
    public static void rotarMatriz90Grados(int[][] matriz) {
        int n = matriz.length;

        // Transponer la matriz original
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = matriz[i][j];
                matriz[i][j] = matriz[j][i];
                matriz[j][i] = temp;
            }
        }

        // Invertir las columnas para la rotación en sentido horario
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matriz[i][j];
                matriz[i][j] = matriz[i][n - 1 - j];
                matriz[i][n - 1 - j] = temp;
            }
        }
    }

    public static void imprimirMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] matriz = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        System.out.println("Matriz original:");
        imprimirMatriz(matriz);

        rotarMatriz90Grados(matriz);

        System.out.println("Matriz rotada 90 grados en sentido horario:");
        imprimirMatriz(matriz);
    }
}