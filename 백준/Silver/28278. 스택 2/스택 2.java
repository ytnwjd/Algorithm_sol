import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> stack = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String inst = br.readLine();
            StringTokenizer st = new StringTokenizer(inst);

            while (st.hasMoreTokens()) {
                int value = Integer.parseInt(st.nextToken());

                switch (value) {
                    case 1:
                        push(stack, Integer.parseInt(st.nextToken()));
                        break;
                    case 2:
                        if(stack.isEmpty()){
                            System.out.println(-1);
                        }
                        else{
                            System.out.println(pop(stack));
                        }
                        break;
                    case 3:
                        System.out.println(size(stack));
                        break;
                    case 4:
                        System.out.println(isEmpty(stack));
                        break;
                    case 5:
                        if(stack.isEmpty()){
                            System.out.println(-1);
                        }
                        else {
                            System.out.println(printNum(stack));
                        }

                }
            }

        }

    }

    public static void push(ArrayList<Integer> arr, int num){
        arr.add(num);
    }

    public static int pop(ArrayList<Integer> arr){
        int num = arr.get(arr.size() - 1);
        arr.remove(arr.size() - 1);

        return num;
    }

    public static int size(ArrayList<Integer> arr){
        return arr.size();
    }

    public static int isEmpty(ArrayList<Integer> arr){
        int num = arr.size();

        if(num == 0){
            return 1;
        }
        else {
            return 0;
        }
    }

    public static int printNum(ArrayList<Integer> arr){
        return arr.get(arr.size() - 1);
    }
}
