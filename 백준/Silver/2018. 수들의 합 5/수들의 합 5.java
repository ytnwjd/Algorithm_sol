import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int str_inx=1, end_idx=1, cnt=1, sum = 1;

        while (end_idx != n) {
            if(sum == n) {
                cnt ++;
                end_idx ++;
                sum += end_idx;
            }
            else if(sum > n){
                sum -= str_inx;
                str_inx++;
            }
            else {
                end_idx++;
                sum += end_idx;
            }

        }

        System.out.println(cnt);

    }
}