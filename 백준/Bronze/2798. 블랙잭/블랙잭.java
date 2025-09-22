import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] numbers = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numbers);
        int max = 0;
        int sum = 0;

        for (int p = 0; p < n; p++){
            int i = p+1;
            int j = n-1;

            while (i < j){
                sum = numbers[p] + numbers[i] +  numbers[j];

                if (sum > m) {  // 합이 더 큰 경우
                    j--;
                }
                else {
                    i++;
                    if((sum >= max)) {
                        max = sum;
                    }
                }
            }

        }

        System.out.println(max);
    }
}