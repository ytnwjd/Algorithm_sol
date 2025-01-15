import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;
        String str = sc.next();

        for (char c: str.toCharArray()){
            sum += Character.getNumericValue(c);
        }

        System.out.println(sum);
    }
}
