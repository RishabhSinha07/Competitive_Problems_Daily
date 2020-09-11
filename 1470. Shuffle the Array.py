# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].  Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution {
    public:
    vector < int > shuffle(vector < int > nums, int n) {
        vector < int > final
        int temp = n
        for(int i=0
            i < n
            i++, temp++){
            final.push_back(nums[i])
            final.push_back(nums[temp])
        }
        return final
    }
}


# Runtime: 4 ms, faster than 99.68% of C++ online submissions for Shuffle the Array.
# Memory Usage: 10.1 MB, less than 6.85% of C++ online submissions for Shuffle the Array.
