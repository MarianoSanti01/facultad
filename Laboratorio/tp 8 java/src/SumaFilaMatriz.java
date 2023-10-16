public class SumaFilaMatriz {
    public static int sumaFilaEspecifica(int[][] matriz, int fila) {
        if (fila < 0 || fila >= matriz.length) {
            throw new IllegalArgumentException("Fila fuera de rango");
        }

        int suma = 0;

        for (int j = 0; j < matriz[fila].length; j++) {
            suma += matriz[fila][j];
        }

        return suma;
    }

    public static void main(String[] args) {
        int[][] matriz = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int filaEspecifica = 1; // Cambia este valor para seleccionar la fila que deseas sumar
        int suma = sumaFilaEspecifica(matriz, filaEspecifica);

        if (filaEspecifica >= 0 && filaEspecifica < matriz.length) {
            System.out.println("La suma de la fila " + filaEspecifica + " es: " + suma);
        } else {
            System.out.println("La fila especificada está fuera de rango.");
        }
    }
}