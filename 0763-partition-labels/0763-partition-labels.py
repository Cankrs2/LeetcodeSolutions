class Solution:
    def partitionLabels(self, s: str):
        L = len(s)
        counter = 1
        seen = {}
        result = []
        last = 0
        for i in range(L):
            seen[s[i]] = i
            print(seen[s[i]])
        for i in range(L):
            last = max(seen[s[i]],last )
            if i == last:
                result.append(counter)
                counter = 1
            else:
                counter +=1
        return result