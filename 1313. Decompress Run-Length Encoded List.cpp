// # We are given a list nums of integers representing a list compressed with run-length encoding.

// # Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

// # Return the decompressed list.

// # Input: nums = [1,2,3,4]
// # Output: [2,4,4,4]
// # Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
// # The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
// # At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

class Solution
{
public:
    vector<int> decompressRLElist(vector<int> &nums)
    {
        vector<int> fin;
        int freq, val;
        for (int i = 0; i < nums.size(); i += 2)
        {
            freq = nums[i];
            val = nums[i + 1];
            while (freq > 0)
            {
                fin.push_back(val);
                --freq;
            }
        }
        return fin;
    }
};

// Runtime: 8 ms, faster than 71.26% of C++ online submissions for Decompress Run-Length Encoded List.
// Memory Usage: 10.3 MB, less than 33.45% of C++ online submissions for Decompress Run-Length Encoded List.