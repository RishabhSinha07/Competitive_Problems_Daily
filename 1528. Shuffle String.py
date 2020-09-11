# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new = [0]*len(indices)
        for i, j in enumerate(indices):
            new[j] = s[i]
        return ''.join(new)


# Runtime: 44 ms, faster than 99.17% of Python3 online submissions for Shuffle String.
# Memory Usage: 13.9 MB, less than 32.29% of Python3 online submissions for Shuffle String.
