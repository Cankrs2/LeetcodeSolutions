class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        freq1 = Counter([v for v in counter1.values()])
        freq2 = Counter([v for v in counter2.values()])
        
        return counter1 == counter2 or (freq1 == freq2 and set(word1)==set(word2))