import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        while (!(s.equals("end"))){
            if (checkStr(s)){  // 문자열 검증 성공
                System.out.printf("<%s> is acceptable. \n", s);
            }
            else {
                System.out.printf("<%s> is not acceptable.\n", s);
            }
            s = br.readLine();
        }

    }

    public static boolean checkStr(String str){

        int gCnt = 0;
        int gCheck = 0;
        int cCnt = 0;
        char prev = 0;

        str = str.replace("ee", "e");
        str = str.replace("oo", "o");

        for (int i = 0; i < str.length(); i++) {

            if (str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
                cCnt = 0;
                gCnt++;
                gCheck++;

                if(str.charAt(i) == prev){
                    return false;
                }

                if(gCnt == 3){
                    /*System.out.println(gCnt);
                    System.out.println(1);*/
                    return false;
                }
            }
            else {
                gCnt = 0;
                cCnt++;

                if(str.charAt(i) == prev){
                    return false;
                }

                if(cCnt == 3){
//                    System.out.println(3);
                    return false;
                }
            }
            prev = str.charAt(i);
        }

        return gCheck != 0;

    }
}
