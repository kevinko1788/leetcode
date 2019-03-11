class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']