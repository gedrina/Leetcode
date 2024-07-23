from collections import Counter

def intersect(nums1, nums2):
    # Count occurrences of each number in nums1
    count1 = Counter(nums1)
    
    # List to store the result
    result = []
    
    # Iterate through nums2
    for num in nums2:
        if num in count1 and count1[num] > 0:
            result.append(num)
            count1[num] -= 1
    
    return result

# Example 
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))  # Output: [2, 2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(intersect(nums3, nums4))  # Output: [4, 9]