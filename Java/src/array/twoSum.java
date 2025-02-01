package array;
import java.util.*;
class twoSum {
    public int[] twoSumf(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        //{value : index}
        for (int i=0; i< nums.length; i++){
            int comp = target-nums[i];
            if(map.containsKey(comp)){
                return new int[] {map.get(comp), i};
            }
            map.put(nums[i],i);
        }
        return new int[] {};
    }



    public static void main(String[] args){
        twoSum s = new twoSum();
        int[] nums={2,7,11,15};
        int target=9;
        int[] res =s.twoSumf(nums, target);
        System.out.println(Arrays.toString(res));
    }
}