import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); //6

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken()); //9

        int[] num = new int[n]; //2 7 4 1 5 3
        st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            num[i]= Integer.parseInt(st.nextToken());
        }
        Arrays.sort(num);   // 1 2 3 4 5 7

        int str=0, end=n-1, cnt=0;

        while(str < end){
            int sum = num[str]+num[end];

            if(sum == m){
                cnt++;
                str++;
                end--;
            }
            else if(sum < m){
                str++;
            }
            else {
                end--;
            }
        }

        System.out.println(cnt);

    }
}