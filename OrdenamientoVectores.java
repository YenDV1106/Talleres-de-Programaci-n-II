import java.util.Random;
import java.util.Scanner;

public class OrdenamientoVectores {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        System.out.print("Ingrese la cantidad de elementos a ordenar: ");
        int cantidad = scanner.nextInt();

        int[] vectorOriginal = new int[cantidad];
        for (int i = 0; i < cantidad; i++) {
            vectorOriginal[i] = random.nextInt(1000) + 1;
        }
        int[] vectorOrdenado = vectorOriginal.clone();
        long inicio = System.currentTimeMillis();
        quickSort(vectorOrdenado, 0, vectorOrdenado.length - 1);
        long fin = System.currentTimeMillis();

        System.out.println("Vector de " + cantidad + " elementos ordenado con éxito.");
        System.out.println("Tiempo de ejecución: " + (fin - inicio) + " ms");

        if (cantidad <= 30) {
            System.out.print("Elementos ordenados: ");
            for (int i = 0; i < cantidad; i++) {
                System.out.print(vectorOrdenado[i] + " ");
            }
            System.out.println();
        }
    }
    public static void quickSort(int[] arr, int bajo, int alto) {
        if (bajo < alto) {
            int pi = particion(arr, bajo, alto);
            quickSort(arr, bajo, pi - 1);
            quickSort(arr, pi + 1, alto);
        }
    }
    private static int particion(int[] arr, int bajo, int alto) {
        int pivote = arr[alto];
        int i = (bajo - 1);
        for (int j = bajo; j < alto; j++) {
            if (arr[j] <= pivote) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[alto];
        arr[alto] = temp;
        return i + 1;
    }
}