import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        int[] check = new int[26];

        for (int i = 0; i < 26; i++) {
            check[i] = -1;
        }

        String word = sc.nextLine();

        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);

            for(int j=0; j < 26; j++){
                if((ch == alphabet.charAt(j)) && (check[j] == -1)){
                    check[j] = i;
                }
            }
            
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(check[i] + " ");
        }
    }
}
