import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = i+1;
        }

        int temp = 0;

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt() - 1; //1
            int y = sc.nextInt() - 1; //4

           for (int j = y; j >= x; j--) {
                temp = arr[j];
                arr[j] = arr[x];
                arr[x] = temp;

                x++;
           }

        }

        for(int num: arr) {
            System.out.print(num + " ");
        }
    }
}
