class Solution:
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=[]
        for word in words:
            mos=""
            for letter in word:
                mos+=mos_table[ord(letter)-97]
            result.append(mos) 
        return(len(set(result)))
            
            
                