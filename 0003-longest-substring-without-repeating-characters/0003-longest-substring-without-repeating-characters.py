class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        result = 0
        left=0
        for i in range(len(s)):
            while s[i] in hash_map:
                del hash_map[s[left]]
                left +=1
            hash_map[s[i]] = hash_map.get(s[i],0)+1
            result = max(result,i-left+1)
        return result