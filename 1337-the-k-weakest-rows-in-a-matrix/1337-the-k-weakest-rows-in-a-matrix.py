class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for index, value in enumerate(mat):
            mat[index] = [value.count(1),index]
        mat.sort()
        return [x[1] for x in mat][:k]
        