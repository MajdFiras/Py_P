# Source : Leetcode ==> Top Interview Questions
# 14. Longest Common Prefix
# difficulty level = easy


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

############################################################

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

############################################################

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

############################################################

# class Solution(object):
#     def longestCommonPrefix(self, strs):

class Solution(object):
    def longestCommonPrefix(self, strs):
        size = len(strs)
        first = strs[0]  # the first element
        if size == 0:
            result = ""
        for x in range(size):
            for y in strs[1:]:
                if (x == len(y) or y[x] != first[x]):
                    return first[0:x]
        return first
