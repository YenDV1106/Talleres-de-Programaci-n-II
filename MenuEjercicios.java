import java.util.Scanner;
public class MenuEjercicios {
    static Scanner leer = new Scanner(System.in);
    public static void main(String[] args) {
        int opcion = 0;
        while (opcion != 4) {
            mostrarMenu();
            opcion = leer.nextInt();

            switch (opcion) {
                case 1:
                    opcionFactorial();
                    break;
                case 2:
                    opcionIMC();
                    break;
                case 3:
                    mostrarPausa();
                    break;
                case 4:
                    System.out.println("Fin del programa");
                    break;
                default:
                    System.out.println("Opcion no valida, intente de nuevo");
            }
        }
    }
    public static void mostrarMenu() {
        System.out.println();
        System.out.println("===== MENU =====");
        System.out.println("1. Calcular factorial");
        System.out.println("2. Calcular IMC");
        System.out.println("3. Hacer una pausa");
        System.out.println("4. Salir");
        System.out.print("Elija una opcion: ");
    }
    public static long calcularFactorial(int numero) {
        long resultado = 1;
        for (int i = 1; i <= numero; i++) {
            resultado = resultado * i;
        }
        return resultado;
    }
    public static void opcionFactorial() {
        System.out.print("Digite un numero: ");
        int numero = leer.nextInt();
        if (numero < 0) {
            System.out.println("No existe el factorial de un numero negativo");
        } else {
            long factorial = calcularFactorial(numero);
            System.out.println("El factorial de " + numero + " es: " + factorial);
        }
    }
    public static double calcularIMC(double pesoKg, double estaturaCm) {
        double estaturaMetros = estaturaCm / 100;
        double imc = pesoKg / (estaturaMetros * estaturaMetros);
        return imc;
    }
    public static void opcionIMC() {
        System.out.print("Digite su estatura en centimetros: ");
        double estatura = leer.nextDouble();
        System.out.print("Digite su peso en Kg: ");
        double peso = leer.nextDouble();
        double imc = calcularIMC(peso, estatura);
        System.out.println("Su IMC es: " + imc);
        if (imc <= 18) {
            System.out.println("IMC con valor bajo");
        } else {
            System.out.println("Mantenga su peso controlado");
        }
    }
    public static void mostrarPausa() {
        System.out.println("Haga una pausa de 5 segundos...");
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            System.out.println("Error en la pausa");
        }
    }
}