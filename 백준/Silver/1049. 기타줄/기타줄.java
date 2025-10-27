import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());   // 끊어진 기타줄의 개수
        int m = Integer.parseInt(st.nextToken());

        int[] pack = new int[m];
        int[] piece = new int[m];
        int result;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            pack[i] = Integer.parseInt(st.nextToken());
            piece[i] = Integer.parseInt(st.nextToken());
        }

        int pack_min = Arrays.stream(pack).min().getAsInt();
        int piece_min = Arrays.stream(piece).min().getAsInt();

        if (n < 6){
            result = Math.min(pack_min, piece_min*n);
        }
        else {
            int pack_maxCnt = n / 6 +1;
            int p=0;
            result = pack_maxCnt * pack_min;
            while (p != pack_maxCnt){
                result = Math.min(result, p * pack_min + piece_min * (n - p*6));
                p++;
            }
        }

        System.out.println(result);

    }
}