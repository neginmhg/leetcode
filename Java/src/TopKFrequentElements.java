/*
 * Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 */

import java.util.*;

public class TopKFrequentElements {
     public static List<Integer> bucketSortTopKFrequent(int[] nums, int k) {
        List<Integer> res = new ArrayList<>();

        Map<Integer,Integer> count = new HashMap<>();
        for(int n:nums){
            int freq=count.getOrDefault(n,0);
            count.put(n, freq+1);
        }

        List<List<Integer>> bucket =new ArrayList<>(nums.length+1);
        for (int i = 0; i < nums.length; i++) {
            bucket.add(new ArrayList<>());
        }

        //***Looping through hashmap***
        for(Map.Entry<Integer,Integer> e: count.entrySet()){
            int key=e.getKey();
            int value =e.getValue();
            bucket.get(value).add(key); 
        }

        for(int i=bucket.size()-1;i>=0;i--){
            for(int n:bucket.get(i)){
                if(res.size()==k){
                    return res;
                }
                res.add(n);
            }
        }
        return res;
     }
     public static void main(String[] args){
        int[] nums = {1,1,1,2,2,3};
        int k = 2;
        List<Integer> res =bucketSortTopKFrequent(nums,k);
        System.out.println(res);
     }

    
}
