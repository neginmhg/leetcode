
/*
 * 
 * Kth Largest Element in an Array
Solved
Medium

Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 */

class FindKthLargest {
    public int FindKthLargestf(int[] nums, int k) {
      int targetIndex = nums.length - k;
        return quickSelect(nums,0, nums.length-1 ,targetIndex);
    }
    public int quickSelect(int[] nums, int l, int r, int targetIndex){
        //set you pivot
        int pivot = nums[r];
        // set a pointer to track where left part and right part get split.
        //pointer should be set at start point.
        int pointer = l;

        //loop between left and right boundaries
        for (int i=l ; i<r; i++){
            if(nums[i]<=pivot){
                int tmp= nums[pointer];
                nums[pointer] = nums[i];
                nums[i] = tmp;
                pointer++;
            }
        }

        //swap the pivot with pointer
        int tmp = nums[pointer];
        nums[pointer] = nums[r];
        nums[r]=tmp;

        //Recursion based on where the pointer is
        if(pointer> targetIndex){
            return quickSelect(nums, l, pointer-1, targetIndex);
        }else if(pointer< targetIndex){
            return quickSelect(nums, pointer+1, r, targetIndex);
        }else{
            return nums[pointer];
        }

    }
}