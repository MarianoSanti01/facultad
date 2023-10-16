public class InvertirFilasMatriz {
    public static void invertirFilas(int[][] matriz) {
        int filas = matriz.length;
        int columnas = matriz[0].length;

        for (int i = 0; i < filas / 2; i++) {
            int[] temp = matriz[i];
            matriz[i] = matriz[filas - 1 - i];
            matriz[filas - 1 - i] = temp;
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

        invertirFilas(matriz);

        System.out.println("Matriz con filas invertidas:");
        imprimirMatriz(matriz);
    }
}