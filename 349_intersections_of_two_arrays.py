def intersection(nums1, nums2):
    # Convert nums1 to a set for efficient lookup
    set1 = set(nums1)
    
    # Use a set to store the intersection
    result = set()
    
    # Iterate through nums2 and check for common elements
    for num in nums2:
        if num in set1:
            result.add(num)
    
    # Convert the result set to a list
    return list(result)


# Example 
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
print(intersection(nums3, nums4))  # Output: [9, 4] 