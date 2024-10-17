from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict=Counter(s)
        print(s_dict)

        if len(s)!=len(t):
            return False

        for word in t:
            if word not in s_dict:
                return False
            if s_dict[word]<=0:
                return False
            s_dict[word]-=1

        return True