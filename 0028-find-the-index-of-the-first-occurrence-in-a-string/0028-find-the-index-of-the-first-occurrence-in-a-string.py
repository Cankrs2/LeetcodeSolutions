class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if (haystack[i: i+len(needle)]) == needle:
                return i
        return -1