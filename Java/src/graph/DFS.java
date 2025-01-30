package graph;
import java.util.*;

public class DFS {
    public List<Integer> traverse(int[][] grid){
        List<Integer> res = new ArrayList<>();

        //edge case
        if(grid==null || grid.length==0 || grid[0].length==0 ){
            return res;
        }

        int ROWS = grid.length;
        int COLS = grid[0].length;

        //Setup visited set to track nodes
        Set<String> visited = new HashSet<>();

        //call dfs
        //params: r,c,grid,visited , res, ROWS,COLS
        dfs(0,0,grid,visited, res, ROWS,COLS);
        return res;
    }
    private void dfs(int r, int c, int[][] grid, Set<String> visited,List<Integer> res, int ROWS, int COLS) {
        //base case:
        if(r<0 || r>=ROWS || c<0 || c>=COLS ||visited.contains(r+","+c)){
            return;
        }
        //Mark it visited
        visited.add(r+","+c);

        //Add to res
        res.add(grid[r][c]);

        //Call dfs on all directions
        int[][] directions = new int[][]{
            {-1,0},
            {1,0},
            {0,1},
            {0,-1},
        };
        for(int[] d:directions){
            int nr = r + d[0];
            int nc = c + d[1];
            dfs(nr,nc,grid,visited, res,ROWS,COLS);
        }
    
    }
    public static void main(String[] args) {
        DFS d = new DFS();
        int[][] grid = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println(d.traverse(grid)); // Output: DFS traversal of grid
    }
}
