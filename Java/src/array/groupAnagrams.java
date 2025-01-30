package array;
/*
 * Medium

Given an array of strings strs, group the 
anagrams
together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
 */

import java.util.*;

class groupAnagrams {
    public List<List<String>> group(String[] strs) {
        //Key: sorted string , value: list of strings
        Map<String, List<String>> map=new HashMap<>();

        //Iterate through each string 
        for(String s: strs){
            //String to array of chars
            char[] charArray = s.toCharArray();
            
            //Sort array of char
            Arrays.sort(charArray);

            //array of char to String
            String sortedS = new String(charArray);

            //check if key is in map
            if(!map.containsKey(sortedS)){
                //new key and value should be a list
                //so new ArrayList for value
                map.put(sortedS, new ArrayList<>());
            }
            map.get(sortedS).add(s);
        }

        //values of map which are each a list should be put into a parent list
        return new ArrayList<>(map.values());

    }
}
