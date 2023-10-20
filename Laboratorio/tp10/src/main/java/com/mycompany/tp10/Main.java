package com.mycompany.tp10;

import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        //EJ1
        Perro p1 = new Perro("Rula", "Mestiza",4);
        p1.ladrar();

        //EJ 4
        Circulo miCirculo = new Circulo(5);
        double area = miCirculo.calcularArea();
        double circunferencia = miCirculo.calcularCircunferencia();
        System.out.println("Área del círculo: " + String.format("%.2f", area) + " unidades cuadradas");
        System.out.println("Circunferencia del círculo: " + String.format("%.2f", circunferencia) + " unidades");

        //EJ6   
        Estudiantes estudiante1 = new Estudiantes("Juan Perez", 20, "12345");
        System.out.println("Nombre del estudiante: " + estudiante1.getNombre());
        System.out.println("Edad del estudiante: " + estudiante1.getEdad());
        System.out.println("Número de identificación del estudiante: " + estudiante1.getNumeroIdentificacion());
        
        //EJ8
         Libro miLibro = new Libro("El Gran Gatsby", "F. Scott Fitzgerald", 1925);

        miLibro.mostrarInformacion();
        
        //EJ10
        CuentaBancaria miCuenta = new CuentaBancaria("123456789");

        miCuenta.depositar(1000.0);
        miCuenta.retirar(500.0);

        System.out.println("Número de cuenta: " + miCuenta.getNumeroCuenta());
        System.out.println("Saldo actual: " + miCuenta.getSaldo());
        
        //EJ12
        Rectangulo miRectangulo = new Rectangulo(5.0, 10.0);

        double area2 = miRectangulo.calcularArea();
        double perimetro = miRectangulo.calcularPerimetro();

        System.out.println("Área del rectángulo: " + area2);
        System.out.println("Perímetro del rectángulo: " + perimetro);
        
        //EJ14
        Coche miCoche = new Coche("Toyota", "Corolla", 2022);

        miCoche.acelerar(50);
        miCoche.frenar(20);

        System.out.println("Marca: " + miCoche.getMarca());
        System.out.println("Modelo: " + miCoche.getModelo());
        System.out.println("Año de fabricación: " + miCoche.getAñoFabricacion());
        System.out.println("Velocidad actual: " + miCoche.getVelocidad() + " km/h");
        
        //EJ16       
        Pelicula miPelicula = new Pelicula("El Padrino", "Francis Ford Coppola", 175);

        miPelicula.mostrarInformacion();
    }
}
