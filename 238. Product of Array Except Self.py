# Given an array nums of n integers where n > 1, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].

# Input:  [1,2,3,4]
# Output: [24,12,8,6]


def productExceptSelf(nums: List[int]) -> List[int]:
    fValue = 1
    final = [1]*len(nums)

    for i in range(len(nums)):
        if i-1 < 0:
            continue
        else:
            fValue *= nums[i-1]
            final[i] *= fValue

    fValue = 1
    for i in range(len(nums)-1, -1, -1):
        if i+1 > len(nums)-1:
            continue
        else:
            fValue *= nums[i+1]
            final[i] *= fValue

    return final


if __name__ == "__main__":
    return productExceptSelf([1, 2, 3, 4])


# Runtime: 124 ms, faster than 83.96% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.4 MB, less than 81.14% of Python3 online submissions for Product of Array Except Self.
