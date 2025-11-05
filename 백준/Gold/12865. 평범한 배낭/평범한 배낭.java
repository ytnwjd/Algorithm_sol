import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());   //물품의 수
        int maxW = Integer.parseInt(st.nextToken());   //최대 무게

        int[] weight = new int[n+1];
        int[] values = new int[n+1];
        int[][] dp = new int[n+1][maxW+1];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            weight[i+1] = Integer.parseInt(st.nextToken());   //무게 6 4 3 5
            values[i+1] = Integer.parseInt(st.nextToken());   //가치 13 8 6 12
        }

        for(int i=0; i<=maxW; i++) {
            dp[0][i] = 0;
        }

        for(int i=1; i<=n; i++) {
            for(int j=0; j<=maxW; j++) {
                if(weight[i] > j){
                    dp[i][j] = dp[i-1][j];
                }
                else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j - weight[i]] + values[i]);
                }
            }
        }

        System.out.println(dp[n][maxW]);


    }
}
