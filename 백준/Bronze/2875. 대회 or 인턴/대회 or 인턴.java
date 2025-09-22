import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); //7
        int m = Integer.parseInt(st.nextToken()); //8
        int k = Integer.parseInt(st.nextToken()); //10

        int result = Math.min(n/2, m);    // 만들어질 수 있는 팀의 수   3
        n -= (result*2);    // 팀 만들고 남은 여학생 수   1
        m -= result;    // 남은 남학생 수 5

        if (n+m-k < 0) {
            k = k-n-m; 

            while (k > 0){
                k -= 3;
                result--;
            }

        }
        System.out.println(result);

    }
}