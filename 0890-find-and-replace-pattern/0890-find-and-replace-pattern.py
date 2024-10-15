class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res=[]

        for word in words:
            w_p_map={}
            p_w_map={}
            can_map=True
            for char_w, char_p in zip(word,pattern):
                if char_w in w_p_map:
                    if w_p_map[char_w]!=char_p:
                        can_map=False
            
                if char_p in p_w_map:
                    if p_w_map[char_p]!=char_w:
                        can_map=False

                w_p_map[char_w]=char_p
                p_w_map[char_p]=char_w

            if can_map==True:
                res.append(word)
        
        return res
