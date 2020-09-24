# Given a string s, return the maximum number of unique substrings that the given string can be split into.

# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

# A substring is a contiguous sequence of characters within a string.


# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

class Solution:

    def fn(self, seen, s):
        max_ = 0
        if s:
            for i in range(1, len(s)+1):
                candidate = s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    max_ = max(max_, 1+self.fn(seen, s[i:]))
                    seen.remove(candidate)
        return max_

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.fn(seen, s)
