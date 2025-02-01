import java.util.*;

// TrieNode class representing each node in the Trie
class TrieNode {
    //{A: Node, B:Node, ........}
    Map<Character, TrieNode> children = new HashMap<>();
    List<String> restaurants = new ArrayList<>();
}

class Trie {
    private TrieNode root;
    private int K; // Max number of restaurants to return per query

    public Trie(int K) {
        this.root = new TrieNode();
        this.K = K;
    }

    // Insert a restaurant name into the Trie
    public void insert(String name) {
        TrieNode node = root;
        for (char c : name.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);

            // Only store restaurant names if there is space for more
            if (node.restaurants.size() < K) {
                node.restaurants.add(name);
            }
        }
    }

    // Search for a list of restaurants that start with the given prefix
    public List<String> search(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return new ArrayList<>(); // No match, return an empty list
            }
            node = node.children.get(c);
        }
        return node.restaurants;
    }
}

public class Solution {

    // Main function to handle restaurant search based on queries
    public static List<List<String>> restaurantSearch(int N, List<String> restaurants, int M, List<String> queries, int K) {
        Trie trie = new Trie(K);

        // Insert all restaurant names into the Trie
        for (String name : restaurants) {
            trie.insert(name.toLowerCase()); // Use lowercase for case-insensitive search
        }

        // Prepare the results for each query
        List<List<String>> result = new ArrayList<>();
        for (String query : queries) {
            List<String> matches = trie.search(query.toLowerCase()); // Get results for the query
            result.add(matches);
        }
        return result;
    }

    public static void main(String[] args) {
        int N = 5;
        List<String> restaurants = Arrays.asList("panda express", "panera bread", "domino's pizza", "pizza hut", "starbucks");
        int M = 3;
        List<String> queries = Arrays.asList("pan", "pi", "star");
        int K = 2;

        List<List<String>> res = restaurantSearch(N, restaurants, M, queries, K);

        // Print the results
        for (List<String> list : res) {
            System.out.println(list);
        }
    }
}
