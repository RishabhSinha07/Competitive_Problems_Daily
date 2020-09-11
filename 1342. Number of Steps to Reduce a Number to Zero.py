# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:  # even
                num = num/2
                count += 1
            else:
                num -= 1
                count += 1
        return count


# Runtime: 28 ms, faster than 81.10% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 65.48% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
