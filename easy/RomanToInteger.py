# Source : Leetcode ==> Top Interview Questions
# 13. Roman to Integer
# difficulty level = easy

#       Symbol       Value
#       I             1
#       V             5
#       X             10
#       L             50
#       C             100
#       D             500
#       M             1000
#       I can be placed before V (5) and X (10) to make 4 and 9.
#       X can be placed before L (50) and C (100) to make 40 and 90.
#       C can be placed before D (500) and M (1000) to make 400 and 900.
#################################################
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#################################################

class Solution(object):
    def romanToInt(self, s):
     str = list(s)
     size = len(str)
     result = 0 
     x=0
     dic = {
         "I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}

     while x < size:
        if x + 1 < size and dic[str[x]] < dic[str[x + 1]]:
         result += dic[str[x + 1]] - dic[str[x]]
         x += 2
        else:
         result += dic[str[x]]
         x += 1
     return result
            
    