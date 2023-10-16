public class ProductoDeMatrices {
    public static int[][] productoMatrices(int[][] matriz1, int[][] matriz2) {
        int filasMatriz1 = matriz1.length;
        int columnasMatriz1 = matriz1[0].length;
        int filasMatriz2 = matriz2.length;
        int columnasMatriz2 = matriz2[0].length;

        if (columnasMatriz1 != filasMatriz2) {
            // No se puede calcular el producto, devuelve una matriz nula
            return null;
        }

        int[][] resultado = new int[filasMatriz1][columnasMatriz2];

        for (int i = 0; i < filasMatriz1; i++) {
            for (int j = 0; j < columnasMatriz2; j++) {
                int suma = 0;
                for (int k = 0; k < columnasMatriz1; k++) {
                    suma += matriz1[i][k] * matriz2[k][j];
                }
                resultado[i][j] = suma;
            }
        }

        return resultado;
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
        int[][] matriz1 = {
            {1, 2, 3},
            {4, 5, 6}
        };

        int[][] matriz2 = {
            {7, 8},
            {9, 10},
            {11, 12}
        };

        int[][] resultado = productoMatrices(matriz1, matriz2);

        if (resultado != null) {
            System.out.println("Producto de matrices:");
            imprimirMatriz(resultado);
        } else {
            System.out.println("No se puede calcular el producto de matrices.");
        }
    }
}