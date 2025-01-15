import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Collection<Integer> numList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            numList.add(sc.nextInt());
        }

        int max = Collections.max(numList);
        int min = Collections.min(numList);

        System.out.printf("%d %d", min, max);
    }
}