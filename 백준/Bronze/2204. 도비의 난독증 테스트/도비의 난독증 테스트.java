import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        while (n != 0){
            String[] words = new String[n];
            String result = "";

            for (int i = 0; i < n; i++){ words[i] = br.readLine(); }

//            if (words[0].compareToIgnoreCase(words[1]) < 0) {
//                result = words[0];
//            } else {
//                result = words[1];
//            }

            result = (words[0].compareToIgnoreCase(words[1]) < 0 ? words[0] : words[1]);
            for (int i = 2; i < words.length; i++){
                result = (result.compareToIgnoreCase(words[i]) < 0 ? result : words[i]);
            }

            System.out.println(result);
            n = Integer.parseInt(br.readLine());
        }

    }
}