def bucketSort(arr):
    # Step 1: Find the maximum and minimum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Step 2: Determine the number of buckets
    bucket_count = max(10, len(arr) // 10)
    
    # Step 3: Calculate the range of each bucket
    bucket_range = (max_val - min_val) / bucket_count
    
    # Step 4: Create the buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Step 5: Distribute the elements into the buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == bucket_count:  # Edge case for the maximum value
            index -= 1
        buckets[index].append(num)
    
    # Step 6: Sort each bucket and concatenate the results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Example usage
arr = [0.42, 0.32, 0.52, 0.26, 0.46]
sorted_arr = bucketSort(arr)
print(sorted_arr)  # Output: [0.26, 0.32, 0.42, 0.46, 0.52]
