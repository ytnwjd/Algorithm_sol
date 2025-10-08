import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        char[] chars = str.toCharArray();
        StringBuilder result = new StringBuilder();

        int i = 0;
        Stack<Character> stack = new Stack<>();
        StringBuilder word = new StringBuilder();   //word 초기화

        while (i < chars.length) {
            if (chars[i] == '<') {
                if(!stack.isEmpty()) {
                    while(!stack.isEmpty()){
                        word.append(stack.pop());
                    }
                    result.append(word);
                    word = new StringBuilder();
                }

                while (chars[i] != '>') {
                    word.append(chars[i]);
                    i++;
                }
                word.append(chars[i]);
                // System.out.println("11= " + word);  //<abc>
            }
            else if (chars[i] == ' '){  // 공백이면 스택 비우고 공백 출력
                while(!stack.isEmpty()){
                    word.append(stack.pop());
                }
                word.append(' ');
                // System.out.println("22= " + word);
            }
            else {
                // System.out.println("33= " + chars[i]);
                stack.push(chars[i]);
            }

            i++;
            result.append(word);
            word = new StringBuilder();
            // System.out.println("!!!!!= " + result);
        }

        while(!stack.isEmpty()){
            result.append(stack.pop());
        }

        System.out.println(result);

    }
}