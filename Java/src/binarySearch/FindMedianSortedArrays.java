package binarySearch;
public class FindMedianSortedArrays {
    public double findMedianSortedArraysf(int[] nums1, int[] nums2) {
        int[] A = nums1;
        int[] B = nums2;

        if(A.length>B.length){
            int[] tmp = A;
            A=B;
            B= tmp;
        }

        int total = A.length+B.length;
        int half = total/2;

        int l=0 , r = A.length-1;
        while(l<=r){
            int i = (l+r)/2;    //middle for A
            int j = half -i-2;   //middle for B

            //2 middles of A
            int ALeft = (i>=0) ? A[i] :Integer.MIN_VALUE;
            int ARight = (i+1<A.length) ? A[i+1] : Integer.MAX_VALUE;


            //2 middles of B
            int BLeft = (j>=0)? B[j] : Integer.MIN_VALUE;
            int BRight = (j+1<B.length)? B[j+1]: Integer.MAX_VALUE;


            //compare
            if(ALeft<= BRight && BLeft<=ARight){
                //found middles
                if(total%2==1){
                    return Math.min(ARight, BRight)/1.0;
                }else{
                    return (Math.max(ALeft,BLeft) + Math.min(BRight,ARight))/2.0;
                }
            }else if(ALeft>BRight){
                r = i-1;
            }else{
                l=i+1;
            }


        }
        return -1.0;
    }
}
