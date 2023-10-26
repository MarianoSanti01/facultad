import java.util.ArrayList;
import java.util.Scanner;

class MarcaAuto {
private String nombre;
public MarcaAuto(String nombre){
    this.nombre=nombre;
}

public String getNombre(){
    return nombre;
}

@Override
    public String toString(){
    return nombre;
}
}
