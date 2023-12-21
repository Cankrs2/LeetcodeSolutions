class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = {}
        for i in magazine:
            hashTable[i] = hashTable.get(i,0) + 1
        for j in ransomNote:
            if j in hashTable:
                if hashTable[j] == 0:
                    return False
                hashTable[j] = hashTable.get(j,0) - 1
            else:
                return False
        return True
        
                