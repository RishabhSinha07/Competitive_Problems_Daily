# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.


# Input: [1,2,3,4]
# Output: "23:41"
import itertools


def largestTimeFromDigits(A):
    max_time = ""
    temp = ()
    p = sorted(list(itertools.permutations(A)), reverse=True)
    for val in p:
        if val[0]*10+val[1] < 24 and val[2] <= 5:
            return max(max_time, str(val[0])+str(val[1])+":"+str(val[2])+str(val[3]))
    return ""


if __name__ == "__main__":
    print(largestTimeFromDigits([1, 2, 3, 4]))


# Runtime: 36 ms, faster than 63.67% of Python3 online submissions for Largest Time for Given Digits.
# Memory Usage: 13.9 MB, less than 48.99% of Python3 online submissions for Largest Time for Given Digits.
