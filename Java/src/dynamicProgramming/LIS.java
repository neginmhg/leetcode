package dynamicProgramming;
import java.util.Arrays;

public class LIS {
    public int lengthOfLIS(int[] nums) {
        //edge case
        if(nums==null || nums.length==0){
            return 0;
        }

        int
        [] dp  = new int[nums.length];
        Arrays.fill(dp,1);

        for(int i=1; i<nums.length;i++){
            for(int j=0; j<i;j++){
                if(nums[i] > nums[j]){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }


        int result=0;
        for(int i=0;i<dp.length;i++){
            result = Math.max(result, dp[i]);
        }
        return result;
    }
    public static void main (String args[]){
        int[] nums= {1,2,3,4,5};
        LIS lis = new LIS();
        int res =lis.lengthOfLIS(nums);
        System.out.println(res);
    }
}