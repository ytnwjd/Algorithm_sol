import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[][] A = new long[n+1][n+1];    // 입력받은 배열
        long[][] D = new long[n+1][n+1];    // 합 배열

        for (int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=1; j<=n; j++){
                A[i][j] =Integer.parseInt(st.nextToken());
            }
        }

        for (int i=1; i<=n; i++){
            for (int j=1; j<=n; j++){
                D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j];
            }
        }

        for(int c=0; c<m; c++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            System.out.println(D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]);
        }

    }
}