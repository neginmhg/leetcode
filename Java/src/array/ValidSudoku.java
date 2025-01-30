package array;
import java.util.Map;
import java.util.HashMap;
import java.util.HashSet;

class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        //have a map for rows; each row would have set of unique numbers
        //have  map for columns; each col would have set of uniue numbers
        //have  map for sections //3 ; each section would have set of unique nubmers


        Map<Integer, HashSet<Character>> rows = new HashMap<>();
        Map<Integer, HashSet<Character>> cols = new HashMap<>();
        Map<String, HashSet<Character>> sections = new HashMap<>();

        for(int r=0;r<board.length;r++){
            for(int c=0; c<board[0].length; c++){
                char current = board[r][c];

                //skip empty cells
                if(current =='.'){
                    continue;
                }

                if(rows.getOrDefault(r, new HashSet<>()).contains(current) || cols.getOrDefault(c, new HashSet<>()).contains(current) ||
                sections.getOrDefault(r / 3 + "," + c / 3, new HashSet<>()).contains(current)){
                    return false;
                }


                //if r, or c or squareKey of this i and j dont have a hashset create one
                //cause we are gonna add current to the set next
                rows.putIfAbsent(r, new HashSet<>() ); 
                cols.putIfAbsent(c,new HashSet<>() );
                String squareKey = r / 3 + "," + c / 3;
                sections.putIfAbsent(squareKey,new HashSet<>() );


                //add current to the hashsets
                rows.get(r).add(current);
                cols.get(c).add(current);
                sections.get(squareKey).add(current);


            }
        }
        return true;


    }
}