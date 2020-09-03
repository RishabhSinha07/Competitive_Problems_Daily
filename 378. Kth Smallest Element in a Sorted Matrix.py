# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.


def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    temp = []
    temp_val = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j])
    return sorted(temp)[k-1]


# Runtime: 184 ms, faster than 86.45% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 19.6 MB, less than 86.32% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
