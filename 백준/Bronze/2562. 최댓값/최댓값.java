import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[9];
        int max = 0;
        int res = 0;

        for (int i = 0; i < 9; i++) {
            int num = sc.nextInt();
            arr[i] = num;

            if(num >= max){
                max = num;
                res = i;
            }
        }

        System.out.printf("%d\n%d", max, res+1);
    }
}