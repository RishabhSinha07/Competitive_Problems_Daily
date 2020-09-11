// Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

// For each kid check if there is a way to distribute extraCandies among the kids
// such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

class Solution
{
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies)
    {
        int maxValue = INT_MIN;
        for (int i = 0; i < candies.size(); i++)
        {
            if (candies[i] > maxValue)
            {
                maxValue = candies[i];
            }
        }
        vector<bool> answer;
        for (int i = 0; i < candies.size(); i++)
        {
            if (candies[i] + extraCandies >= maxValue)
            {
                answer.push_back(true);
            }
            else
            {
                answer.push_back(false);
            }
        }
        return answer;
    }
};

// Runtime: 4 ms, faster than 86.22% of C++ online submissions for Kids With the Greatest Number of Candies.
// Memory Usage: 9 MB, less than 59.04% of C++ online submissions for Kids With the Greatest Number of Candies.