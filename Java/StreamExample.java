import java.util.*;
import java.util.stream.*;
import java.util.function.*;

public class StreamExample {

    public static void main(String[] args) {

        // Sample data
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date");

        // Example 1: Creating a Stream from a Collection
        Stream<Integer> numberStream = numbers.stream();
        Stream<String> wordStream = words.stream();

        // Example 2: Filter (Intermediate Operation)
        // Filtering even numbers
        System.out.println("Even numbers:");
        numberStream.filter(n -> n % 2 == 0)   // filter even numbers
                    .forEach(System.out::println);  // terminal operation

        // Example 3: Map (Intermediate Operation)
        // Squaring each number in the list
        System.out.println("\nSquares of numbers:");
        numbers.stream()
               .map(n -> n * n) // transform each element
               .forEach(System.out::println);

        // Example 4: Sort (Intermediate Operation)
        // Sorting words by length
        System.out.println("\nWords sorted by length:");
        words.stream()
             .sorted(Comparator.comparingInt(String::length))  // Sort by length of the string
             .forEach(System.out::println);

        // Example 5: Reduce (Terminal Operation)
        // Sum all numbers
        int sum = numbers.stream()
                         .reduce(0, (a, b) -> a + b); // reduce to a single value
        System.out.println("\nSum of numbers: " + sum);

        // Example 6: Collect (Terminal Operation)
        // Collect even numbers into a new list
        List<Integer> evenNumbers = numbers.stream()
                                           .filter(n -> n % 2 == 0)
                                           .collect(Collectors.toList());
        System.out.println("\nEven numbers collected into a list: " + evenNumbers);

        // Example 7: ForEach (Terminal Operation)
        // Print each word in uppercase
        System.out.println("\nWords in uppercase:");
        words.stream()
             .map(String::toUpperCase)
             .forEach(System.out::println);

        // Example 8: Find First (Terminal Operation)
        // Find first even number
        Optional<Integer> firstEven = numbers.stream()
                                             .filter(n -> n % 2 == 0)
                                             .findFirst();  // returns Optional
        firstEven.ifPresent(n -> System.out.println("\nFirst even number: " + n));

        // Example 9: Count (Terminal Operation)
        // Count how many words start with 'b'
        long count = words.stream()
                          .filter(w -> w.startsWith("b"))
                          .count();
        System.out.println("\nCount of words starting with 'b': " + count);

        // Example 10: Any Match (Terminal Operation)
        // Check if any word contains 'a'
        boolean anyMatch = words.stream()
                                .anyMatch(w -> w.contains("a"));
        System.out.println("\nAny word contains 'a': " + anyMatch);

        // Example 11: All Match (Terminal Operation)
        // Check if all words have length greater than 4
        boolean allMatch = words.stream()
                                .allMatch(w -> w.length() > 4);
        System.out.println("\nAll words have length > 4: " + allMatch);

        // Example 12: None Match (Terminal Operation)
        // Check if no word contains 'z'
        boolean noneMatch = words.stream()
                                 .noneMatch(w -> w.contains("z"));
        System.out.println("\nNo word contains 'z': " + noneMatch);

        // Example 13: FlatMap (Intermediate Operation)
        // Flatten a List of Lists of integers
        List<List<Integer>> listOfLists = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(4, 5),
                Arrays.asList(6, 7, 8)
        );
        List<Integer> flatList = listOfLists.stream()
                                            .flatMap(Collection::stream)  // flatten the list
                                            .collect(Collectors.toList());
        System.out.println("\nFlattened List: " + flatList);

        // Example 14: Grouping By (Collectors)
        // Grouping words by their first character
        Map<Character, List<String>> groupedWords = words.stream()
                                                         .collect(Collectors.groupingBy(w -> w.charAt(0)));
        System.out.println("\nWords grouped by their first character: " + groupedWords);

        // Example 15: Partitioning By (Collectors)
        // Partition numbers into odd and even
        Map<Boolean, List<Integer>> partitionedNumbers = numbers.stream()
                                                                .collect(Collectors.partitioningBy(n -> n % 2 == 0));
        System.out.println("\nNumbers partitioned into odd and even: " + partitionedNumbers);
    }
}
