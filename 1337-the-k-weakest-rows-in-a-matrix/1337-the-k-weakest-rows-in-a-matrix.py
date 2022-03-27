class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []
        for index, value in enumerate(mat):
            temp.append([value.count(1),index])
        temp.sort()
        return [x[1] for x in temp][:k]
        