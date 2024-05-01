class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_index = 0
        new_string = ""
        for i in range(len(word)):
            if word[i] == ch:
                ch_index = i
                break
        counter = ch_index
        while counter>=0:
            new_string = new_string + word[counter] 
            counter-=1
        new_string = new_string + word[ch_index+1:]
        return new_string