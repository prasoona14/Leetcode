class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_new = s.split()

        if len(pattern)!=len(s_new):
            return False

        s_t_map = {}
        t_s_map = {}

        for char_s, char_t in zip(s_new,pattern):
            if char_s in s_t_map:
                if s_t_map[char_s]!=char_t:
                    return False
            
            if char_t in t_s_map:
                if t_s_map[char_t]!=char_s:
                    return False
            
            s_t_map[char_s]=char_t
            t_s_map[char_t]=char_s
            
        return True