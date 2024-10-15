class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        total_length=0

        for word in words:
            word_count = Counter(chars)
            can_form = True

            for char in word:
                if word_count[char]==0:
                    can_form = False
                    break                    
                word_count[char]-=1

            if can_form:
                total_length += len(word)
        return total_length
        