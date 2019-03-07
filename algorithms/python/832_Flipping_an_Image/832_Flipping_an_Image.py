class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = [a[::-1] for a in A]
        A = [[1 - x for x in a]for a in A]
        return A