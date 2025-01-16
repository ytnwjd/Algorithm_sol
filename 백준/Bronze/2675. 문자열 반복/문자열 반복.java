import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            String str = sc.next();
            String result = "";

            for (int j = 0; j < str.length(); j++){
                char ch = str.charAt(j);
                for (int k = 0; k < num; k++){
                    result += ch;
                }
            }
            System.out.println(result);
        }
        
    }
}
