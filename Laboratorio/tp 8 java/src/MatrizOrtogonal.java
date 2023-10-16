import java.util.Arrays;

public class MatrizOrtogonal {
    public static boolean esMatrizOrtogonal(int[][] matriz) {
        int filas = matriz.length;
        int columnas = matriz[0].length;

        // Verificar si la matriz es cuadrada
        if (filas != columnas) {
            return false;
        }

        // Verificar si la matriz es ortogonal
        int[][] transpuesta = new int[filas][columnas];

        // Calcular la transpuesta de la matriz
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                transpuesta[i][j] = matriz[j][i];
            }
        }

        // Calcular la matriz inversa
        int[][] identidad = new int[filas][columnas];
        for (int i = 0; i < filas; i++) {
            identidad[i][i] = 1;
        }

        // Verificar si la matriz es igual a su transpuesta
        return Arrays.deepEquals(matriz, transpuesta);
    }

    public static void main(String[] args) {
        int[][] matriz = {
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 1}
        };

        if (esMatrizOrtogonal(matriz)) {
            System.out.println("La matriz es ortogonal.");
        } else {
            System.out.println("La matriz no es ortogonal.");
        }
    }
}