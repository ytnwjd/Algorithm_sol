import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        char[] chars = str.toCharArray();
        int n = sc.nextInt();

        System.out.println(chars[n-1]);
    }
}
