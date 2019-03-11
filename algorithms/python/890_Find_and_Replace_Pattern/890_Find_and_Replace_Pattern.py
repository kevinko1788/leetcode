class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_index = self.findPattern(pattern)
        result = []
        for word in words:
            if self.findPattern(word) == pattern_index:
                result.append(word)
        return result
    
    def findPattern(self,pattern: str)-> str: 
        pattern_list = []
        pattern_index =""
        for c in pattern:
            if c not in pattern_list:
                pattern_list.append(c)
                pattern_index+= str(pattern_list.index(c))
            else:
                pattern_index+= str(pattern_list.index(c))
        return pattern_index