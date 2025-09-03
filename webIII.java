package Equipo_6;
import java.util.Scanner;
public class webIII {
    public static void main(String[] args){
        Scanner sc=new Scanner (System.in);
        System.out.println("Ingrese su nombre para imprimir el saludo");
        String nombre=sc.nextLine();
        System.out.println("buen dia "+nombre+", este es nuestro equipo:");
        System.out.println("1. Univ. Colque Huchani Jhesica Laura ");
        System.out.println("2. Univ. Aguilar Machicado Nils Reiner ");
        System.out.println("3. Univ. Guitierres Herrera Mayra Fabiola ");
        System.out.println("4. Univ. Layme Gonza Vidal  ");
    }
}
