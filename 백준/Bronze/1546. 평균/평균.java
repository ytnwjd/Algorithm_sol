import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<Integer> grade = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            grade.add(sc.nextInt());
        }

        System.out.println(cal_sum(grade)/n);
    }

    public static double cal_sum(ArrayList<Integer> grade) {
        int max = Collections.max(grade);
        double sum = 0;

        for(double i : grade) {
            i = (i/max)*100;
            sum += i;
        }

        return sum;
    }
}
