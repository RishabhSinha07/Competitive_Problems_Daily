
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.


def findKthLargest(self, nums: List[int], k: int) -> int:
    nums = sorted(nums)
    return nums[len(nums)-k]


if __name__ == "__main__":
    inp = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(inp, k))


# Runtime: 60 ms, faster than 96.19% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 28.48% of Python3 online submissions for Kth Largest Element in an Array.
