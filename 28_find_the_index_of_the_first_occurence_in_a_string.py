def find_first_occurrence(haystack, needle):
    # Check for empty needle
    if needle == "":
        return 0
    
    # Loop through the haystack
    for i in range(len(haystack) - len(needle) + 1):
        # Check if the substring matches the needle
        if haystack[i:i + len(needle)] == needle:
            return i
    
    # If needle is not found, return -1
    return -1

# Test the function
haystack = "sadbutsad"
needle = "sad"
result = find_first_occurrence(haystack, needle)
print(result)  # Output: 0

# Test the function with another example
haystack = "leetcode"
needle = "leeto"
result = find_first_occurrence(haystack, needle)
print(result)  # Output: -1
        
    