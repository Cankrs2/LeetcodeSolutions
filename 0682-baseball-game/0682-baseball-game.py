class Solution:
    def calPoints(self, operations) -> int:
        record = []
        total = 0
        for operation in operations:
            if operation == "C":
                record.pop(-1)
            elif operation == "D":
                record.append(record[-1] * 2)
            elif operation == "+":
                val = record[-1]  + record[-2]
                record.append(val)
            else:
                record.append(int(operation))
        for i in record:
            total += i
        return (total)