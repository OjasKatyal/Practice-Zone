#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        tmp = abs(x)
        
        rev_num = 0

        while(tmp != 0):
            digit = tmp % 10
            tmp //= 10
            rev_num = rev_num * 10 + digit

        if x < 0:
            rev_num *= -1
        
        if -2**31 <= rev_num <= 2**31 - 1:
            return rev_num
        else:
            return 0
        
# @lc code=end

