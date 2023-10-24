package com.mycompany.tp10;

public class Coche {
    private String marca;
    private String modelo;
    private int añoFabricacion;
    private int velocidad; // Añadimos un atributo para llevar un registro de la velocidad

    public Coche(String marca, String modelo, int añoFabricacion) {
        this.marca = marca;
        this.modelo = modelo;
        this.añoFabricacion = añoFabricacion;
        this.velocidad = 0; // Inicializamos la velocidad en 0 al crear el coche
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public int getAñoFabricacion() {
        return añoFabricacion;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public void acelerar(int incrementoVelocidad) {
        if (incrementoVelocidad > 0) {
            velocidad += incrementoVelocidad;
            System.out.println("El coche está acelerando. Velocidad actual: " + velocidad + " km/h");
        } else {
            System.out.println("Error: El incremento de velocidad debe ser mayor que 0.");
        }
    }

    public void frenar(int decrementoVelocidad) {
        if (decrementoVelocidad > 0 && decrementoVelocidad <= velocidad) {
            velocidad -= decrementoVelocidad;
            System.out.println("El coche está frenando. Velocidad actual: " + velocidad + " km/h");
        } else {
            System.out.println("Error: El decremento de velocidad debe ser mayor que 0 y no puede exceder la velocidad actual.");
        }
    }}