package com.mycompany.tp10;

public class Circulo{
    private double radio;

    public Circulo(){
    }

    public Circulo(double radio){
        this.radio=radio;
    }
    
    public double getRadio() {
        return radio;
    }
    
    public void setRadio(double radio) {
        this.radio = radio;
    }

    public double calcularArea() {
        double area = Math.PI * Math.pow(radio, 2);
        return area;
    }

    public double calcularCircunferencia() {
        double circunferencia = 2 * Math.PI * radio;
        return circunferencia;
    }
}

