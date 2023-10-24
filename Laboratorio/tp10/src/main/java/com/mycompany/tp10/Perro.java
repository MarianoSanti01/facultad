package com.mycompany.tp10;

public class Perro {
    private String nombre;
    private String raza;
    private int edad;
    public Perro() {
    }
    public Perro(String nombre, String raza, int edad) {
        this.nombre = nombre;
        this.raza = raza;
        this.edad = edad;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getRaza() {
        return raza;
    }
    public void setRaza(String raza) {
        this.raza = raza;
    }
    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public void ladrar() {
        System.out.println("Guau, guau");
    }
    public void datos() {
        System.out.println("Nombre del perro: "+nombre);
        System.out.println("Raza del perro : "+raza);
        System.out.println("Edad del perro: "+edad);
    }
}
<<<<<<< HEAD:Laboratorio/tp-10/src/Perro.java

=======
>>>>>>> cc5963581711ae16cfffce0ece954108d1761957:Laboratorio/tp10/src/main/java/com/mycompany/tp10/Perro.java
