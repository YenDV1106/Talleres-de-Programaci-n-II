import java.util.Scanner;
public class Calculadora{
public static void main (String []args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Ingrese el primer número: ");
    double num1 = sc.nextDouble();
    System.out.print("Ingrese el segundo número: ");
    double num2 = sc.nextDouble();
    double suma = num1 + num2;
    double multiplicacion = num1 * num2;
    System.out.println("La suma de " + num1 + " y " + num2 + " es: " + suma);
    System.out.println("La multiplicación de " + num1 + " y " + num2 + " es: " + multiplicacion);
    sc.close();
}
}