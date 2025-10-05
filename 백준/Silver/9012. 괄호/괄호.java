import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();
            String result = "YES";

            for (int j = 0; j < str.length(); j++) {
                if(str.charAt(j) == '(') {
                    stack.push(str.charAt(j));
                }
                else {
                    if(!stack.isEmpty()) { stack.pop(); }
                    else {
                        result = "NO";
                        break;
                    }
                }
            }
            if(!stack.isEmpty()) { result = "NO"; }
            System.out.println(result);
        }
    }
}