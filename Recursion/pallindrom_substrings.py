"""
Problem Statement: Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
"""

# Time Complexity: O(N) effectively evaluating corresponding mirrored array blocks strictly bounded to the span of strings.
# Space Complexity: O(N) evaluating allocations instancing independent mirrored slice equivalents validating values intrinsically.
def is_pallindrome(s):
    # Short-hand validator resolving identity matching reversed index strings dynamically identifying configurations correctly.
    return s == s[::-1]

# def pallindrome_partion_substrings(s, last_partition=-1, result=None, partitions_at=None):
#     if result is None:
#         result = []
#     if partitions_at is None:
#         partitions_at = []

#     if last_partition == len(s) - 1:
#         substrings = []
#         print(partitions_at)
#         for i in range(len(partitions_at)):
#             item = s[0 if i == 0 else partitions_at[i-1] + 1 : partitions_at[i] + 1]
#             substrings.append(item)

#         if substrings and all(is_pallindrome(x) for x in substrings):
#             result.append(substrings)
#         return

#     for i in range(last_partition + 1, len(s)):
#         partitions_at.append(i)
#         pallindrome_partion_substrings(s, i, result, partitions_at)
#         partitions_at.pop()

#     return result
# Time Complexity: O(2^N * N) spanning across extensive configurations evaluating substring checks natively upon traversal branches overlapping.
# Space Complexity: O(N) extending localized configurations bounding variables within path sequence limits caching states inherently.
def pallindrome_partion_substrings(s, last_solved_partition=0, result=None, partitions_at=None):
    # Backtracking recursively traversing independent boundaries systematically testing segmentation overlaps triggering validations strictly correctly.
    # Constructs configurations conditionally bounding structural index blocks processing natively validating results conditionally correctly natively.
    if partitions_at is None:
        partitions_at = []
    if result is None:
        result = []
    if last_solved_partition == len(s):
        substrings = []
        # print(partitions_at)
        for i in range(len(partitions_at)):
            # print(f"start index:{0 if i==0 else partitions_at[i-1]+1}")
            # print(f"end index:{partitions_at[i]+1}")
            item = s[0 if i==0 else partitions_at[i-1]+1: partitions_at[i]+1]
            # print(f"item:{item}")
            substrings.append(item)
        if len(partitions_at)>0:
            last_partition_at = partitions_at[len(partitions_at)-1]
            if last_partition_at != len(s)-1:
                remaining_item = s[last_partition_at+1:]
                substrings.append(remaining_item)

        if substrings and all(is_pallindrome(x) for x in substrings) and substrings not in result:
            result.append(substrings)
        return

    partitions_at.append(last_solved_partition)
    pallindrome_partion_substrings(s, last_solved_partition+1, result, partitions_at)
    partitions_at.pop()
    pallindrome_partion_substrings(s, last_solved_partition+1, result, partitions_at)
    return result



print(pallindrome_partion_substrings("aabc"))


