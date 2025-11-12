import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] prefixSum = new int[10];
        int n = Integer.parseInt(br.readLine());
        prefixSum[0] = n;

        for (int i=1; i<10; i++){
            n = Integer.parseInt(br.readLine());
            prefixSum[i] = prefixSum[i-1] + n;
        }

        int gap = 1000;
        int result = 0;
        for(int num : prefixSum) {
            int tmp = 100 - num;
            if(tmp < 0) {
                tmp = Math.abs(tmp);
                if(tmp <= gap){
                    gap = tmp;
                    result = num;
                }
            }
            else {
                if(tmp <= gap){
                    gap = tmp;
                    result = num;
                }
            }
        }

        System.out.println(result);
    }
}
