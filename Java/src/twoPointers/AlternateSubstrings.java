package twoPointers;
/*
 * Write a Java program to count the number of alternate substrings in a given string. A substring is considered an alternate substring if it consists of consecutive characters that alternate (e.g., in a binary string, the substring alternates between 0 and 1).

Example:
Input: "010101"
Output: 15

Explanation: The substrings that alternate are:
01, 10, 01, 10, 01, 010, 101, 0101, 1010, 01010, 10101, etc.
 */
public class AlternateSubstrings {
    public static int count(String s){
        int count =0;
        //asume the first char starts a new alternating substirng group
        int length =1;

        //start from 1 to length
        for (int i = 1; i < s.length(); i++) {
            //compare this with prev
            if(s.charAt(i)!=s.charAt(i-1)){
                //found alternating
                length ++;
            }else{
                //same char so end this group
                count += (length*(length-1))/2;
                length=1;   //reset length 
                //After a non-alternating character is found, you start over with a new group of alternating substrings. The length = 1 represents the first character of this new group.
            }
            //add the last run of alternating substrings
            count += (length*(length-1))/2;
            return count;
        }

    }
}
