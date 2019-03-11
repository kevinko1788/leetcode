class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        index = 0
        words=""
        #row finding
        for row in board:
            if 'R' in row:
                words = "".join(z for z in row if z != '.')
                if "Rp" in words:
                    result +=1
                if "pR" in words:
                    result +=1
                index = row.index('R')
        #col finding
        words = ''.join(board[i][index] for i in range(len(board)) if board[i][index] != '.')
                
        if "Rp" in words:
            result +=1
        if "pR" in words:
            result +=1   
        return result