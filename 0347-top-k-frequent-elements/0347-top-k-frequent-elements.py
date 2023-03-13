class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        answer =[]
        for i in nums:
            if i in hash:
                hash[i] = 1 + hash.get(i,0)
            else:
                hash[i] = 1
        keys = list(hash.keys())        
        values = list(hash.values())    
        while k >0:
            result = 0
            for i in range(len(values)):
                if values[i] > result:
                    result = values[i]
                    index = i
            answer.append(keys[index])
            values.pop(index)
            keys.pop(index)
            
            k-=1
        return answer