class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows-1):
            row= []
            temp = [0] + result[-1] + [0]
            for j in range(len(result[-1]) +1):
                row.append(temp[j]+temp[j+1])
            result.append(row)
        return result