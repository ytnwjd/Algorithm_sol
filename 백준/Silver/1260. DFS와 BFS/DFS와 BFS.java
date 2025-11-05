import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n+1];

        for(int i=1; i<=n; i++){
            graph[i] = new ArrayList<>();    // 초기화
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            graph[node1].add(node2);
            graph[node2].add(node1);
        }

        for(int i=1; i<=n; i++){
            Collections.sort(graph[i]);
        }

        visited = new boolean[n+1];
        dfs(v);
        System.out.println();
        visited = new boolean[n+1];
        bfs(v);
    }

    public static void dfs(int v){
        System.out.print(v + " ");
        visited[v] = true;

        for(int w : graph[v]){
            if(!visited[w]){
                dfs(w);
            }
        }
    }

    public static void bfs(int v){
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        visited[v] = true;

        while(!q.isEmpty()){
            int w = q.poll();
            System.out.print(w + " ");
            for(int x : graph[w]){
                if(!visited[x]){
                    q.add(x);
                    visited[x] = true;
                }
            }
        }
    }
}

