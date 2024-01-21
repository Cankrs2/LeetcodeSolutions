class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        string = []
        a_pointer = len(a)-1
        for i in range(len(b) - 1, -1, -1):
            total = 0
            if a_pointer == -1:
                if carry == 1 and b[i] == "1":
                    string.insert(0,"0")
                elif carry ==1 and b[i] =="0":
                    string.insert(0,"1")
                    carry -=1
                else:
                    string.insert(0,b[i])
                continue 
            total = int(b[i]) + int(a[a_pointer]) + carry
            carry = 0
            if total == 1:
                string.insert(0,"1")
            elif total > 1:
                if total == 3:
                    string.insert(0,"1")
                    carry = 1
                else:   
                    string.insert(0,"0")
                    carry=1
            else:
                string.insert(0,"0")
            a_pointer -=1
            
            
        while a_pointer >= 0:
            if carry == 1 and a[a_pointer] == "1":
                string.insert(0,"0")
            elif carry ==1 and a[a_pointer] == "0":
                string.insert(0,"1")
                carry -=1
            else:
                string.insert(0,a[a_pointer])
            a_pointer-=1;
            
        if carry == 1:
            string.insert(0,"1")
        
        return ''.join(string)
    