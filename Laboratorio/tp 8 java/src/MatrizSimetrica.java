public class MatrizSimetrica {
    public static boolean esMatrizSimetrica(int[][] matriz) {
        int filas = matriz.length;
        int columnas = matriz[0].length;

        if (filas != columnas) {
            // La matriz no es cuadrada, por lo tanto no puede ser simétrica.
            return false;
        }

        // Creamos una matriz transpuesta
        int[][] matrizTranspuesta = new int[filas][columnas];

        // Llenamos la matriz transpuesta intercambiando filas y columnas
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matrizTranspuesta[i][j] = matriz[j][i];
            }
        }

        // Comparamos la matriz original con la transpuesta
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] != matrizTranspuesta[i][j]) {
                    return false; // Las matrices no son iguales, por lo tanto no es simétrica.
                }
            }
        }

        return true; // Si llegamos aquí, la matriz es simétrica.
    }

    public static void main(String[] args) {
        int[][] matriz = {
            {1, 2, 3},
            {2, 4, 5},
            {3, 5, 6}
        };

        if (esMatrizSimetrica(matriz)) {
            System.out.println("La matriz es simétrica.");
        } else {
            System.out.println("La matriz no es simétrica.");
        }
    }
}