# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
    track = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                continue
            if (i, j) in track or (j, i) in track:
                continue
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

            track.append((i, j))

    for li in matrix:
        po1, po2 = 0, len(li)-1
        while po1 < po2:
            li[po1], li[po2] = li[po2], li[po1]
            po1 += 1
            po2 -= 1
    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(matrix))
