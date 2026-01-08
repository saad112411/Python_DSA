def most_occuring_element_offset(arr):
    if not arr:
        return None
    # Step 1: Find the range of numbers
    min_val = min(arr)
    max_val = max(arr)
    # Step 2: Create a count array with reduced size
    range_size = max_val - min_val + 1
    count_arr = [0] * range_size

    for num in arr:
        index = num - min_val  # Calculate index using the offset
        count_arr[index] += 1

    max_count = -1
    result_index = -1
    for i in range(len(count_arr)):
        if count_arr[i] > max_count:
            max_count = count_arr[i]
            result_index = i         
    # Step 5: Convert the index back to the original number
    return result_index + min_val
arr = [-105, -105, -105, 104 ,104, 104, 106]
print(most_occuring_element_offset(arr)) # Output: 105