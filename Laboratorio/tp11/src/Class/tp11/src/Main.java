import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    ArrayList<MarcaAuto> marcasDeAutos = new ArrayList<>();
    Scanner scanner = new Scanner(System.in);
    boolean continuar = true;

    while(continuar){
        System.out.println("Ingresa una marca de auto");
        String nombreMarca = scanner.nextLine();

        MarcaAuto marca= new MarcaAuto(nombreMarca);
        marcasDeAutos.add(marca);

        System.out.println("Deseas ingresar otra marca? si/no");
        String respuesta = scanner.nextLine().toLowerCase();
        if(respuesta.equals("no")){
            continuar = false;
        }
    }
        System.out.println("Marcas de autos guardadas:");
        for (MarcaAuto marca : marcasDeAutos) {
            System.out.println(marca.getNombre());
        }
        }
    EquipoDeFutbol equipo = new EquipoDeFútbol();

        equipo.agregarJugador("Lionel Messi", 10);
        equipo.agregarJugador("Sergio Ramos", 4);
        equipo.agregarJugador("Neymar Jr.", 11);

        equipo.listarPlantilla();

        equipo.eliminarJugador(4);

        equipo.listarPlantilla();
}
