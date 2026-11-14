import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

/*
 Jen Jesús Leal Ruíz
 Método: Cifrado César recursivo. Se utiliza una función recursiva que recorre 
 la cadena índice por índice sumando 3 al código ASCII de cada carácter para 
 encriptar, y restando 3 para desencriptar.
 */
public class EncriptadorApp {

    static final String NOMBRE_ARCHIVO = "frase_secreta.txt";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion = 0;

        do {
            System.out.println("\n  MENU  ");
            System.out.println("1. Ingresar frase y encriptar");
            System.out.println("2. Desencriptar y mostrar frase");
            System.out.println("3. Salir");
            System.out.print("Elige una opcion: ");

            if (scanner.hasNextInt()) {
                opcion = scanner.nextInt();
                scanner.nextLine();
            } else {
                scanner.next();
                continue;
            }

            switch (opcion) {
                case 1:
                    System.out.print("Escribe la frase que quieres guardar: ");
                    String frase = scanner.nextLine();
                    String fraseEncriptada = encriptarRecursivo(frase, 0);
                    guardarEnArchivo(fraseEncriptada);
                    System.out.println("¡Frase encriptada y guardada con exito (reemplazo la anterior)!");
                    break;

                case 2:
                    String fraseLeida = leerDesdeArchivo();
                    if (fraseLeida != null && !fraseLeida.isEmpty()) {
                        String fraseDesencriptada = desencriptarRecursivo(fraseLeida, 0);
                        System.out.println("Frase desencriptada: " + fraseDesencriptada);
                    } else {
                        System.out.println("Aun no hay ninguna frase guardada en el archivo.");
                    }
                    break;

                case 3:
                    System.out.println("Saliendo del programa...");
                    break;

                default:
                    System.out.println("Opcion no valida, intenta de nuevo.");
            }
        } while (opcion != 3);

        scanner.close();
    }

    public static String encriptarRecursivo(String texto, int indice) {
        if (indice >= texto.length()) {
            return "";
        }
        char c = (char) (texto.charAt(indice) + 3);
        return c + encriptarRecursivo(texto, indice + 1);
    }

    public static String desencriptarRecursivo(String texto, int indice) {
        if (indice >= texto.length()) {
            return "";
        }
        char c = (char) (texto.charAt(indice) - 3);
        return c + desencriptarRecursivo(texto, indice + 1);
    }

    public static void guardarEnArchivo(String texto) {
        try (FileWriter escritor = new FileWriter(NOMBRE_ARCHIVO, false)) {
            escritor.write(texto);
        } catch (IOException e) {
            System.out.println("Ocurrio un error al escribir el archivo.");
        }
    }

    public static String leerDesdeArchivo() {
        StringBuilder resultado = new StringBuilder();
        try (BufferedReader lector = new BufferedReader(new FileReader(NOMBRE_ARCHIVO))) {
            String linea;
            while ((linea = lector.readLine()) != null) {
                resultado.append(linea);
            }
        } catch (IOException e) {
            return null;
        }
        return resultado.toString();
    }
}