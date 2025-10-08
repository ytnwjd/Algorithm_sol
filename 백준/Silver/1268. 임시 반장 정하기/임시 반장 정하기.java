import java.awt.color.ICC_ColorSpace;
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());    // 학생 수
        int[][] cls = new int[n][5];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = st.countTokens();
            for (int j = 0; j < a; j++) {
                cls[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int max = 0;
        int maxIndex = 0;

        for(int i = 0; i < n; i++) {
            int cnt = 0;

            for(int j = 0; j < n; j++) {
                    for (int k = 0; k < 5; k++) {
                        if(i!=j & cls[i][k]==cls[j][k]){
//                            System.out.println("!!" + " i="+ i + " j="+ j + " k="+ k+" !!");
//                            System.out.println(cls[i][k] + " " + cls[j][k]);
                            cnt++;
                            k=5;
                            break;
                        }
                    }
            }
            // System.out.println("i="+i + " cnt="+cnt);

            if(cnt > max){
                max = cnt;
                maxIndex = i;
            }
        }

        System.out.println(maxIndex+1);

    }
}