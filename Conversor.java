import java.util.Scanner;
public class Conversor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingresa la distancia en kilómetros: ");
        double kilometros = sc.nextDouble();
        double metros = kilometros * 1000;
        double centimetros = kilometros * 100000;
        System.out.println(kilometros + " kilómetros son equivalentes a " + metros + " metros y " + centimetros + " centímetros.");
        sc.close();
    }
}
