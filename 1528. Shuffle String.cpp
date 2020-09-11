// Given a string s and an integer array indices of the same length.

// The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

// Return the shuffled string.

class Solution
{
public:
    string restoreString(string s, vector<int> &indices)
    {
        string n = s;
        for (int i = 0; i < indices.size(); i++)
        {
            n[indices[i]] = s[i];
        }
        return n;
    }
};

// Runtime: 16 ms, faster than 74.00% of C++ online submissions for Shuffle String.
// Memory Usage: 15.5 MB, less than 22.22% of C++ online submissions for Shuffle String.