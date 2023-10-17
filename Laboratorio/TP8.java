import java.lang.Math;
import java.util.Scanner;
import java.util.Arrays;
public class TP8 {
    public static void main(String[] args) {

    }

    //EJERCICIO 1
    public static int[][] product_matrices(int[][] matriz1, int[][] matriz2) {
        int[][] matriz3 = new int[matriz1.length][matriz1[0].length];
        for (int i = 0; i < matriz1.length; i++) {
            for (int j = 0; j < matriz1[0].length; j++) {
                matriz3[i][j] = matriz1[i][j] * matriz2[i][j];
            }
        }
        return matriz3;
    }

    //EJERCICIO 2
    public static int[][] sumMatrices(int[][] matriz1, int[][] matriz2) {
        int[][] matriz3 = new int[matriz1.length][matriz1[0].length];
        for (int i = 0; i < matriz1.length; i++) {
            for (int j = 0; j < matriz1[0].length; j++) {
                matriz3[i][j] = matriz1[i][j] + matriz2[i][j];
            }
        }
        return matriz3;
    }

    //EJERCICIO 3
    public static int[][] transposeMatriz(int[][] matriz) {
        int[][] transposedMatriz = new int[matriz.length][matriz[0].length];
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                transposedMatriz[j][i] = matriz[i][j];
            }
        }
        return transposedMatriz;
    }

    //EJERCICIO 4
    public static boolean simetricSmatrix(int[][] matrix) {
        int[][] matrix2 = transposeMatriz(matrix);
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] != matrix2[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    //EJECRICIO 5
    public static int[][] escalarProduct(int[][] matrix, int product) {
        int[][] matrix2 = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix2[i][j] = matrix[i][j] * product;
            }
        }
        return matrix2;
    }

    //EJERCICIO 6
    public static int calcularSumaMatriz(int[][] matriz) {
        int suma = 0;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                suma += matriz[i][j];
            }
        }

        return suma;
    }

    //EJERCICIO 7
    public static int[] findMAxElementAndPosition(int[][] matrix) {
        int maxValue = matrix[0][0];
        int row = 0;
        int column = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] > maxValue) {
                    maxValue = matrix[i][j];
                    row = i;
                    column = j;
                }
            }
        }
        int data[] = {maxValue, row, column};
        return data;
    }

    //JERCICIO 8
    public static int sumaFilaEspecifica(int[][] matriz, int fila) {
        int suma = 0;

        for (int j = 0; j < matriz[fila].length; j++) {
            suma += matriz[fila][j];
        }

        return suma;
    }

    //EJERCICIO 9
    public static boolean diagonalMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (i != j) {
                    if (matrix[i][j] != 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    //EJERCICIO 10
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

    //EJERCICIO 11
    public static int[] countPeersAndOdds(int[][] matrix) {
        int peers = 0;
        int odds = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] % 2 == 0) {
                    peers++;
                } else {
                    odds++;
                }
            }
        }
        int[] data = {peers, odds};
        return data;
    }

    //EJERCICIO 12
    public static void rotateMatriz(int[][] matrix) {
        int lon = matrix.length;
        for (int i = 0; i < (lon / 2); i++) {
            for (int j = 0; j < (matrix[0].length - 1 - i); j++) {
                int aux = matrix[i][j];
                matrix[i][j] = matrix[lon - 1 - j][i];
                matrix[lon - 1 - j][i] = matrix[lon - 1 - i][lon - 1 - j];
                matrix[lon - 1 - i][lon - 1 - j] = matrix[i][lon - 1 - i];
                matrix[i][lon - 1 - i] = aux;
            }
        }
    }

    //EJERCICIO 13
    public static int countElementMatrix(int[][] matrix, int toSearch) {
        int counter = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == toSearch) {
                    counter++;
                }
            }
        }
        return counter;
    }
    //EJERCICIO 14
        public static void invertirFilas ( int[][] matriz){
            int filas = matriz.length;
            for (int i = 0; i < filas / 2; i++) {
                int[] temp = matriz[i];
                matriz[i] = matriz[filas - 1 - i];
                matriz[filas - 1 - i] = temp;
            }
        }
        //EJERCICIO 16
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
    //EJERCICIO 17
        public static int[] minElementsInRow( int [][] matrix){
            int [] data=new int[matrix.length];
            for(int i =0;i<matrix.length;i++){
                int min  = matrix[i][0];
                for(int j=0;j<matrix[0].length;j++){
                    if (matrix[i][j]<min){
                        min=matrix[i][j];
                    }
                }
                data[i]=min;
            }
            return data;
        }
    //EJERCICIO 18
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

    }