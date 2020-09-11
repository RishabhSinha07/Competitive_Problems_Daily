# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(S)):
            if J.find(S[i]) != -1:
                count += 1
        return count


# Runtime: 32 ms, faster than 62.10% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.9 MB, less than 39.72% of Python3 online submissions for Jewels and Stones.
