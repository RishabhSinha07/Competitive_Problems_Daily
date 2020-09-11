// Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

// Return the answer in an array.

class Solution
{
public:
    vector<int> smallerNumbersThanCurrent(vector<int> &nums)
    {
        vector<int> f;
        for (int i = 0; i < nums.size(); i++)
        {
            int temp = nums[i];
            int count = 0;
            for (int j = 0; j < nums.size(); j++)
            {
                if (i != j)
                {
                    if (nums[j] < temp)
                    {
                        ++count;
                    };
                };
            };
            f.push_back(count);
        };
        return f;
    };
};

// Runtime: 40 ms, faster than 49.68% of C++ online submissions for How Many Numbers Are Smaller Than the Current Number.
// Memory Usage: 10.2 MB, less than 78.65% of C++ online submissions for How Many Numbers Are Smaller Than the Current Number.
// Next challenges: