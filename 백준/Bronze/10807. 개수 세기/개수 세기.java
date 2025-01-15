import java.util.ArrayList;
import java.util.Collection;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Collection<Integer> numList = new ArrayList<>();

        for (int i = 1; i <= n; i++){
            int num = sc.nextInt();
            numList.add(num);
        }

        int find = sc.nextInt();
        int cnt = 0;

       for (Integer num : numList){
           if (num == find){
               cnt ++;
           }
       }

       System.out.println(cnt);
    }
}