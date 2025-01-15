import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] numList = new int[n];

        for (int i = 0; i < n; i++){
            int num = sc.nextInt();
            numList[i] = num;
        }

        int find = sc.nextInt();
        int cnt = 0;

       for (int i = 0; i < n; i++){
           if (numList[i] == find){
               cnt ++;
           }
       }

       System.out.println(cnt);
    }
}