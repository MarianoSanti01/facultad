import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.HashSet;
public class TP9 {
    public static void main(String[] args) {
        /*EJERCICIO 1
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);*/
        /*EJERCICIO 2
        ArrayList<String>names=new ArrayList<>();
        names.add("juan");names.add("elliot");names.add("big boss");*/
        /*EJERCICIO 3
        for (int num:numbers){
            System.out.println(num);
         }*/
        /*EJERCICIO 4
        ArrayList<Character>characters=new ArrayList<Character>();
        characters.add('a');characters.add('b');characters.add('c');
        System.out.println(characters.size());*/
        /*EJERCICIO 5
        ArrayList<String>names=new ArrayList<>();
        names.add("juan");names.add("elliot");names.add("big boss");
        names.remove(2);*/
        /*EJERCICIO 6
        ArrayList<Integer> numbers=new ArrayList<>();
        boolean verification=numbers.isEmpty();
        if(verification){
            System.out.println("el array esta vacio");
        }
        else {
            System.out.println("el array no eta vacio");
        }*/
        /*EJERCICIO 7
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        int biggest=numbers.get(0);
        for (int num:numbers){
            if(num>biggest){
                biggest=num;
            }
        }
        System.out.println(biggest);*/
        /*EJERCICIO 8
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        ArrayList<Integer>numbers2=new ArrayList<>(numbers);*/
        /*EJERCICICIO 9
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        ArrayList<Integer>numbers2=new ArrayList<>();
        int lon=numbers.size();
        for(int i=lon-1;i>=0;i--){
            numbers2.add(numbers.get(i));
        }*/
        /*10
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        ArrayList<Integer>numbers2=new ArrayList<>();
        numbers2.add(6);numbers2.add(7);numbers2.add(8);numbers2.add(9);numbers2.add(10);
        ArrayList<Integer>numbers3=new ArrayList<>(numbers);
        numbers3.addAll(numbers2);*/
        /*EJERCICIO 11
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        Iterator<Integer>i=numbers.iterator();
        while (i.hasNext()){
            int j= i.next();
            if(j%2==0){
                i.remove();
            }
        }
        for(int num:numbers){
            System.out.println(num);
        }*/
        /*EJERCICIO 12
            ArrayList<String>names=new ArrayList<>();
            names.add("juan");names.add("elliot");names.add("big boss");
            int index=names.indexOf("elliot");
            System.out.println(index);
         */
        /*EJERCICIO 13
        ArrayList<Integer> numbers=new ArrayList<>();
        ArrayList<Integer> newNumbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        newNumbers.add(1);newNumbers.add(2);newNumbers.add(4);newNumbers.add(4);newNumbers.add(5);
        int index;
        if(numbers.size() != newNumbers.size()){
            System.out.println("los arreglos no son iguales");
        }
        else{
            for(int num:numbers){
                index=numbers.indexOf(num);
                if(num != newNumbers.get(index)){
                    System.out.println("los elementos indice "+index+" no son iguales");
                }
                else{
                    System.out.println("los elementos indice "+index+" son iguales");
                }
            }
        }*/
        /*EJERCICIO 14
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        int lowest=numbers.get(0);
        for (int num:numbers){
            if(num<lowest){
                lowest=num;
             }
         }
         System.out.println(lowest);
         */
        /*EJERCICIO 15
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);
        int total=0;
        for (int num:numbers){
           total += num;
        }
        System.out.println(total);
         */
        /*EJERCICIO 16
        ArrayList<String>names=new ArrayList<>();
        names.add("juan");names.add("elliot");names.add("big boss");
        String chain="";
        for(String name:names){
            chain += name+" ";
        }
        System.out.println(chain);
         */
        /*EJERCICIO 17 TERMINAR NO FUNCIONA
        ArrayList<String>names=new ArrayList<>();
        ArrayList<String>names2=new ArrayList<>();
        names.add("juan");names.add("juan");names.add("lain");names.add("elliot");names.add("lain");
        names2.add("juan");names2.add("juan");names2.add("lain");names2.add("elliot");names2.add("lain");
        Iterator<String>i=names.iterator();
        String j,k;
        while (i.hasNext()) {
            j = i.next();
            while (i.hasNext()){
                j = i.next();
                if(names2.contains(j)){
                    i.remove();
                }
            }
        }
        for(String name:names){
            System.out.println(name);
        }*/
        /*EJERCICIO 18
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(0);numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);numbers.add(1);
        int i,total=0;
        for(i=0;i<numbers.size();i+=2){
            total+=numbers.get(i);
        }
        System.out.println(total);
         */
        /*EJERCICIO 19
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(0);numbers.add(1);numbers.add(2);numbers.add(3);numbers.add(4);numbers.add(5);numbers.add(1);
        int toSearch=5;
        for(int number:numbers){
            if (number==toSearch){
                System.out.println("numero encontrado en poscicion "+numbers.indexOf(1));
                break;
            }
        }
         */
        /*EJERCICIO 20 encontrar cadenas ams larga
        ArrayList<String>names=new ArrayList<>();
        names.add("juan");names.add("simon");names.add("elliot");names.add("lain");
        int len;
        String longest= names.get(0);
        for(String name:names){
            len=name.length();
            if(longest.length()<len){
                longest=name;
            }
        }
        System.out.println(longest);
         */
        /*EJERICICIO 21
        ArrayList<Integer> numbers=new ArrayList<>();
        numbers.add(10);numbers.add(5);numbers.add(4);numbers.add(1);numbers.add(3);numbers.add(2);
        float total=0;
        for(int num:numbers){
            total+=num;
        }
        float avarage=(total/numbers.size());
        System.out.print(avarage);
         */
        /*EJERCICIO 22
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(2);numbers.add(1);numbers.add(3);numbers.add(5);numbers.add(4);numbers.add(6);
        Collections.sort(numbers);
        for (int num:numbers) {
            System.out.println(num);
        }
         */
        /*EJERCICIO 23
        Crea un ArrayList de números enteros y elimina todos los elementos mayores que un valor específico.
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(2);numbers.add(1);numbers.add(3);numbers.add(5);numbers.add(4);numbers.add(6);
        int value=4;
        Iterator<Integer>i=numbers.iterator();
        while (i.hasNext()){
            int j= i.next();
            if(j>value){
                i.remove();
            }
        }
        for (int num:numbers){
            System.out.println(num);
        }
         */
        /*EJERCICIO 24 24.	Encuentra la cantidad de veces que un elemento específico aparece en un ArrayList de cadenas.
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(2);numbers.add(1);numbers.add(3);numbers.add(5);numbers.add(1);numbers.add(6);
        int value=1;
        int counter=0;
        for (int num:numbers){
            if(num==value){
                counter++;
            }
        }
        System.out.println("el numero "+value+" se repite "+counter+" veces");
         */
        /*EJERCICIO 25
        ArrayList<String>names=new ArrayList<>();
        names.add("juan");names.add("simon");names.add("elliot");names.add("lain");
        Collections.sort(names);
        for(String name:names){
            System.out.println(name);
        }
         */
    }
}
