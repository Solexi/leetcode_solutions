class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        
        # iterate from right to left
        i = len(a) - 1
        j = len(b) - 1
        
        # add corresponding digits and carry
        while i >= 0 or j >= 0:
            sum = carry
            
            if i >= 0:
                sum += int(a[i])
                i -= 1
            
            if j >= 0:
                sum += int(b[j])
                j -= 1
            
            # calculate carry and result digit
            carry = sum // 2
            digit = sum % 2
            res += str(digit)
        
        # add carry to result if it's not zero
        if carry:
            res += str(carry)
        
        # reverse the result string and return
        return res[::-1]
