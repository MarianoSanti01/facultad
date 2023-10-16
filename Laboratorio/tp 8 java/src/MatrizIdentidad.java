public class MatrizIdentidad {
    public static int[][] generarMatrizIdentidad(int n) {
        int[][] matriz = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    matriz[i][j] = 1; // Diagonal principal
                } else {
                    matriz[i][j] = 0; // Otros elementos
                }
            }
        }

        return matriz;
    }

    public static void main(String[] args) {
        int n = 3; // Cambia este valor para el tamaño de la matriz identidad que deseas

        int[][] matrizIdentidad = generarMatrizIdentidad(n);

        System.out.println("Matriz Identidad " + n + "x" + n + ":");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrizIdentidad[i][j] + " ");
            }
            System.out.println();
        }
    }
}