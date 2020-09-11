// Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums.

class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        for (int i = 1; i < nums.size(); i++)
        {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};

// Runtime: 4 ms, faster than 92.09% of C++ online submissions for Running Sum of 1d Array.
// Memory Usage: 8.6 MB, less than 73.94% of C++ online submissions for Running Sum of 1d Array.