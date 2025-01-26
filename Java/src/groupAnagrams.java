import java.util.*;

class groupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        // HashMap to store the sorted string as key and the list of anagrams as value
        Map<String, List<String>> map = new HashMap<>();
        
        // Iterate through each string in the input array
        for (String str : strs) {
            // Convert the string to a char array and sort it
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            // Convert the sorted char array back to a string
            String sortedStr = new String(charArray);
            
            // If the sorted string is already a key in the map, add the original string to the list
            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            map.get(sortedStr).add(str);
        }
        
        // Return the values of the map, which are the grouped anagrams
        return new ArrayList<>(map.values());
    }
}
