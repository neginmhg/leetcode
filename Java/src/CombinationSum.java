import java.util.*;



class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();

        //call backtrack
        backtrack(candidates, target, 0, new ArrayList<>(), 0,res);

        return res;
    }

    private void backtrack(int[] candiates, int target, int start, List<Integer> current, int sum, List<List<Integer>> res){

        //base case
        if(sum==target){
            //When we call new ArrayList<>(current), we are creating a new copy of the current list at that moment. This ensures that res stores a separate copy of the list, not a reference to current.
            res.add(new ArrayList<>(current));
            return;
        }

        //invalid
        if(sum>target){
            return;
        }

        //explore each candidate
        for(int i=start; i<candiates.length;i++){
            current.add(candiates[i]);
            backtrack(candiates, target, i, current, sum+candiates[i], res);
            current.remove(current.size()-1);
        }
    }

    public static void main(String[] args) {
        CombinationSum sol = new CombinationSum();

        // Test cases
        int[] candidates1 = {2, 3, 6, 7};
        int target1 = 7;
        System.out.println(sol.combinationSum(candidates1, target1));  // Output: [[2, 2, 3], [7]]

        int[] candidates2 = {2, 3, 5};
        int target2 = 8;
        System.out.println(sol.combinationSum(candidates2, target2));  // Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    }
}