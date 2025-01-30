import java.util.*;
public class BFS {
    public  List<Integer> traverse(int[][] grid){
        List<Integer> res = new ArrayList<>();
        //Edge Case
        if(grid==null){
            return new ArrayList<>();
        }
        //Get Lenth
        int ROWS= grid.length;
        int COLS= grid[0].length;

        // SetUp Directions
        int[][] directions = new int[][]{
            {-1, 0},  // Up
            {1, 0},   // Down
            {0, -1},  // Left
            {0, 1}    // Right
        };

        //Setup Queue storing [row,col]
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0,0});

        //Setup Visit Set storing String of r,c
        Set<String> visited = new HashSet<>();
        visited.add("0,0");

        //While q
        while(!q.isEmpty()){
            // store the size before processing the queue
            int size = q.size();
            for (int i = 0; i < size; i++) {
                //poll from q
                int[] cell = q.poll();
                int r = cell[0];
                int c= cell[1];

                //PROCESS IT
                res.add(grid[r][c]);
                //ADD NEIGHBORS TO Q AND VISITED
                for(int[] dr :directions){
                    //System.out.println(d[0]+d[1]);
                    int nr = dr[0]+r ;
                    int nc = c+dr[1];

                    //boundary check
                    if(!visited.contains(nr+","+nc) && nr>=0 && nr<ROWS && nc>=0 && nc<COLS){
                        q.add(new int[]{nr,nc});
                        visited.add(nr+","+nc);
                    }
                }
                
            }
        }
        return res;
    }

    public static void main(String[] args){
        BFS b = new BFS();
        int[][] grid={{1,2,3},{4,5,6},{7,8,9}};
        System.out.println(b.traverse(grid));
    }
}
