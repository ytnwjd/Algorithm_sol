import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static boolean[] used;
    static int[] result;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        used = new boolean[N + 1];
        result = new int[M];

        backtrack(0);

        System.out.print(sb.toString());
    }

    static void backtrack(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            sb.append('\n');
            return;
        }

        for (int num = 1; num <= N; num++) {
            if (!used[num]) {
                used[num] = true;
                result[depth] = num;
                backtrack(depth + 1);
                used[num] = false;
            }
        }
    }
}