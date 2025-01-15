import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> arr  = new ArrayList<>();

        for (int i=0; i<10; i++) {
            int num = sc.nextInt() % 42;
            exist(arr, num);
        }

        System.out.println(arr.toArray().length);
    }

    public static void exist(ArrayList<Integer> arr, int num){
        for(int n: arr){
            if(n == num){
                return;
            }
        }
        arr.add(num);
    }
}
