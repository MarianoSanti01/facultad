import java.util.ArrayList;

class Jugador {
    private String nombre;
    private int numeroCamiseta;

    public Jugador(String nombre, int numeroCamiseta) {
        this.nombre = nombre;
        this.numeroCamiseta = numeroCamiseta;
    }

    public String getNombre() {
        return nombre;
    }

    public int getNumeroCamiseta() {
        return numeroCamiseta;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + " | Número de Camiseta: " + numeroCamiseta;
    }
}

class EquipoDeFútbol {
    private ArrayList<Jugador> plantilla;

    public EquipoDeFutbol() {
        plantilla = new ArrayList<>();
    }

    public void agregarJugador(String nombre, int numeroCamiseta) {
        Jugador jugador = new Jugador(nombre, numeroCamiseta);
        plantilla.add(jugador);
        System.out.println("Jugador agregado: " + jugador.toString());
    }

    public void eliminarJugador(int numeroCamiseta) {
        for (Jugador jugador : plantilla) {
            if (jugador.getNumeroCamiseta() == numeroCamiseta) {
                plantilla.remove(jugador);
                System.out.println("Jugador eliminado: " + jugador.toString());
                return;
            }
        }
        System.out.println("No se encontró un jugador con el número de camiseta " + numeroCamiseta);
    }

    public void listarPlantilla() {
        System.out.println("Plantilla del equipo:");
        for (Jugador jugador : plantilla) {
            System.out.println(jugador.toString());
        }
    }
}
