class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        hash_map = {}
        max_len = 0
        while right < len(s):
            while s[right] in hash_map:
                del hash_map[s[left]]
                left += 1
            hash_map[s[right]] = right
            max_len = max(max_len,right - left + 1)
            right += 1
        return max_len