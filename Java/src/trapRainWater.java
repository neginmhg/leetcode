import java.util.PriorityQueue;

class trapRainWater {
    public int trapRainWaterf(int[][] heightMap) {
        //edge cases
        if(heightMap==null || heightMap.length==0 || heightMap[0].length==0){
            return 0;
        }

        int ROWS = heightMap.length;
        int COLS = heightMap[0].length;

        //setup a heap(priorty queue)
        PriorityQueue<Cell> minHeap = new PriorityQueue<>((a,b)-> a.height - b.height);

        //visit array
        boolean[][] visited = new boolean[ROWS][COLS];


        //Add LEFT & RIGHT boundary cells to min heap and visited
        for(int i=0; i<ROWS; i++){
            //left most column
            minHeap.offer(new Cell(i, 0 , heightMap[i][0]));
            //right most column
            minHeap.offer(new Cell(i, COLS-1 , heightMap[i][COLS-1]));
            //add to visited
            visited[i][0]=true;
            visited[i][COLS-1]=true;
        }

        //Add TOP & BOTTOM boundary cells to min heap and visited
        for(int j=0; j<COLS; j++){
            //top most column
            minHeap.offer(new Cell(0, j , heightMap[0][j]));
            //bottom most column
            minHeap.offer(new Cell(ROWS-1, j , heightMap[ROWS-1][j]));
            //add to visited
            visited[0][j]=true;
            visited[ROWS-1][j]=true;
        }

        //Directions array
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};

        int result =0;
        //process each wall in heap
        while(!minHeap.isEmpty()){
            Cell wall = minHeap.poll();

            //Check 4 neighbots
            for(int[] direction:directions){
                int nr = wall.row + direction[0];
                int nc = wall.col + direction[1];


                //check if this neighbot is in bound and not visited
                if(nr>=0 && nr<ROWS && nc>=0 && nc<COLS && !visited[nr][nc]){
                    //mark it visite
                    visited[nr][nc]=true;
                    int neighborheight = heightMap[nr][nc];
                    //calculate trapped water if it traps if not 0
                    int newWater = Math.max(0, wall.height - neighborheight);
                    result+=newWater;

                    //add/update this neighbor as a new wall in heap
                    int Newneighborheight= Math.max(wall.height,neighborheight ) ;
                    minHeap.offer(new Cell(nr,nc, Newneighborheight));
                        
                }

            }
        }
        return result;





    }
}


class Cell{
    int row;
    int col;
    int height;

    Cell(int row, int col, int height){
        this.row = row;
        this.col = col;
        this.height=height;
    }
}